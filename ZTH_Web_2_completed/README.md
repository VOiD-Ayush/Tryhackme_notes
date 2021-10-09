# ZTH_Web_2 

> VOiD | Saturday 07 August 2021 10:30:20 AM IST

My IP : 10.17.6.109
Target IP : 


# Intro
```
The purpose of this room, is to show the more subtle vulnerabilities. These vulns won't get you RCE, or LFI, but they will allow you to access sensitive information that a client would want to keep protected.

The topics that will be covered in this room are:

- IDOR

- Forced Browsing

- API based Authentication Bypass



You can do this room with minimal experience, but I will be using some pentesting terms that if you don't know, you should research.

```


# Section 1 [IDOR]

Intro
```
IDOR, or Insecure Direct Object Reference, is the act of exploiting a misconfiguration in the way user input is handled, to access resources you wouldn't ordinarily be able to access.

For example, let's say we're logging into our bank account, and after correctly authenticating ourselves, we get taken to a URL like this https://example.com/bank?account_number=1234. On that page we can see all our important bank details, and a user would do whatever they needed to do and move along their way thinking nothing is wrong.

There is however a potentially huge problem here, a hacker may be able to change the account_number parameter to something else like 1235, and if the site is incorrectly configured, then he would have access to someone else's bank information.

```

Challenge
```
The credentials are:

noot:test1234

Try and exploit IDOR to get the flag!

Port: 80

http://10.10.139.55/note.php?note=0

Flag : flag{fivefourthree}

```

# Section 2 [Forced Browsing]

Intro
```
Forced browsing is the art of using logic to find resources on the website that you would not normally be able to access. For example let's say we have a note taking site, that is structured like this. http://example.com/user1/note.txt. It stands to reason that if we did http://example.com/user2/note.txt we may be able to access user2's note. 

Taking this a step further, if we ran wfuzz on that url, we could enumerate users we don't know about, as well as get their notes. This is quite devastating, because we can then run further attacks on the users we find, for example bruteforcing each user we find, to see if they have weak passwords.
```

Challenge
```bash
ffuf -w /usr/share/wordlists/dirb/big.txt -u http://10.10.139.55:81/FUZZ/note.txt
password                [Status: 200, Size: 20, Words: 1, Lines: 2]
flag : flag{forcednooting}

```

# Section 3 [API Bypass]

Intro
```
This is a bit of a unique one, as it can basically be anything. APIs are by definition incredibly versatile, and finding out how to exploit them, will require a lot of research and effort by the hacker. The following situation is only one possible scenario out of a near infinite number.

```
flag{test1234}



