#!/bin/python3

import socket
import sys
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def recv(s):
    try:
        data = s.recv(1024)
        return data
    except Exception as e:
        print(str(e))

def decrypt(key, iv, cText, tag):
	#Create AES GCM decryptor object
	decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag),
	backend = default_backend()).decryptor()
	#Return decrypted text
	return (decryptor.update(cText)+decryptor.finalize())


host = "10.10.153.13"
port = 4000
server = (host, port)
iv = b'secureivl337' #Hardcoded for ease
key = b'thisisaverysecretkeyl337'

#Create socket *No need to connect as using UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Get initial message
s.sendto(b"hello", server)
print(recv(s).decode("utf-8"))
s.sendto(b"ready", server)
data= recv(s)
print(data,end="\n\n")
checksum = data[104:136].hex() #Convert to hex to make comparison easier
print("checksum =",checksum)

while True:
	#Get the cipher text
	s.sendto(b"final", server)
	cText = bytes(recv(s))
	print("cText = ",cText)
	#Get the tag
	s.sendto(b"final", server)
	tag = bytes(recv(s))
	print("tag = ",tag)
	#Decrypt
	pText = decrypt(key, iv, cText, tag)
	print("pText = ",pText.decode("utf-8"))
	#Compare
	if hashlib.sha256(pText).hexdigest() != checksum:
		continue
	else:
		print(f"\n\nThe flag is: {pText}")
		break



