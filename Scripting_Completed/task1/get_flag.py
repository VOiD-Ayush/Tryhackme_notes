#!/bin/python3

import base64

print("[+] Opening file")
file = open("b64.txt",'r')

enc=file.read()

print("[+] Decoding ")

for i in range(50):
	enc=base64.b64decode(enc)

print("[+] Decoded text is ",end='')
print(enc.decode("UTF-8"))
