# John_The_Ripper 

# first task hashes

```bash
# using hash-identifier to find hash type

hash1.txt: 2e728dd31fb5949bc39cac5a9f066498
Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

john hash1.txt --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt
biscuit


hash2.txt: 1A732667F3917C0F4AA98BB13011B9090C6F8065
Possible Hashs:
[+] SHA-1
[+] MySQL5 - SHA-1(SHA-1($pass))

john hash2.txt  --wordlist=/usr/share/wordlists/rockyou.txt 
kangeroo


hash3.txt: D7F4D3CCEE7ACD3DD7FAD3AC2BE2AAE9C44F4E9B7FB802D73136D4C53920140A
Possible Hashs:
[+] SHA-256
[+] Haval-256

john hash3.txt --format=Raw-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt 
microphone


hash4.txt: c5a60cc6bbba781c601c5402755ae1044bbf45b78d1183cbf2ca1c865b6c792cf3c6b87791344986c8a832a0f9ca8d0b4afd3d9421a149d57075e1b4e93f90bf
Possible Hashs:
[+] SHA-512
[+] Whirlpool

john hash4.txt --format=whirlpool --wordlist=/usr/share/wordlists/rockyou.txt 
colossal

```

# TASK 5
```bash
john ntlm.txt --format=NT --wordlist=/usr/share/wordlists/rockyou.txt  
mushroom

```

# TASK 6

Cracking Hashes from /etc/shadow
The /etc/shadow file is the file on Linux machines where password hashes are stored. It also stores other information, such as the date of last password change and password expiration information. It contains one entry per line for each user or user account of the system. This file is usually only accessible by the root user- so in order to get your hands on the hashes you must have sufficient privileges, but if you do- there is a chance that you will be able to crack some of the hashes.




Unshadowing
John can be very particular about the formats it needs data in to be able to work with it, for this reason- in order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The basic syntax of unshadow is as follows:

unshadow [path to passwd] [path to shadow]

unshadow - Invokes the unshadow tool

[path to passwd] - The file that contains the copy of the /etc/passwd file you've taken from the target machine

[path to shadow] - The file that contains the copy of the /etc/shadow file you've taken from the target machine

Example Usage:

unshadow local_passwd local_shadow > unshadowed.txt

Note on the files

When using unshadow, you can either use the entire /etc/passwd and /etc/shadow file- if you have them available, or you can use the relevant line from each, for example:

FILE 1 - local_passwd

Contains the /etc/passwd line for the root user:

root:x:0:0::/root:/bin/bash

FILE 2 - local_shadow

Contains the /etc/shadow line for the root user:

root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::


Cracking
We're then able to feed the output from unshadow, in our example use case called "unshadowed.txt" directly into John. We should not need to specify a mode here as we have made the input specifically for John, however in some cases you will need to specify the format as we have done previously using: --format=sha512crypt

john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

```bash

echo "root:x:0:0::/root:/bin/bash" > local_passwd
echo "root:\$6\$Ha.d5nGupBm29pYr\$yugXSk24ZljLTAZZagtGwpSQhb3F2DOJtnHrvk7HI2ma4GsuioHp8sm3LJiRJpKfIf7lZQ29qgtH17Q/JDpYM/:18576::::::"
unshadow local_passwd local_shadow > hash
john hash --wordlist=/usr/share/wordlists/rockyou.txt  
1234             (root)

```


# Single Crack Mode
So far we've been using John's wordlist mode to deal with brute forcing simple., and not so simple hashes. But John also has another mode, called Single Crack mode. In this mode, John uses only the information provided in the username, to try and work out possible passwords heuristically, by slightly changing the letters and numbers contained within the username.



Word Mangling
The best way to show what Single Crack mode is,  and what word mangling is, is to actually go through an example:

If we take the username: Markus

Some possible passwords could be:

Markus1, Markus2, Markus3 (etc.)
MArkus, MARkus, MARKus (etc.)
Markus!, Markus$, Markus* (etc.)
This technique is called word mangling. John is building it's own dictionary based on the information that it has been fed and uses a set of rules called "mangling rules" which define how it can mutate the word it started with to generate a wordlist based off of relevant factors for the target you're trying to crack. This is exploiting how poor passwords can be based off of information about the username, or the service they're logging into.


GECOS
John's implementation of word mangling also features compatibility with the Gecos fields of the UNIX operating system, and other UNIX-like operating systems such as Linux. So what are Gecos? Remember in the last task where we were looking at the entries of both /etc/shadow and /etc/passwd? Well if you look closely You can see that each field is seperated by a colon ":". Each one of the fields that these records are split into are called Gecos fields. John can take information stored in those records, such as full name and home directory name to add in to the wordlist it generates when cracking /etc/shadow hashes with single crack mode.



Using Single Crack Mode
To use single crack mode, we use roughly the same syntax that we've used to so far, for example if we wanted to crack the password of the user named "Mike", using single mode, we'd use:

john --single --format=[format] [path to file]

--single - This flag lets john know you want to use the single hash cracking mode.

Example Usage:

john --single --format=raw-sha256 hashes.txt

A Note on File Formats in Single Crack Mode:

If you're cracking hashes in single crack mode, you need to change the file format that you're feeding john for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example- we would change the file hashes.txt

From:

1efee03cdcb96d90ad48ccc7b8666033

To

mike:1efee03cdcb96d90ad48ccc7b8666033


Practical
Now you're familiar with the Syntax for John's single crack mode, download the attached hash and crack it, assuming that the user it belongs to is called "Joker".


```bash
john hash --single --format=raw-md5  
JoK3r
```
