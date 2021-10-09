# Tyler 

# Target IP : 10.10.18.196

# My IP : 10.8.226.18

PORT     STATE SERVICE      REASON
22/tcp   open  ssh          syn-ack
80/tcp   open  http         syn-ack
139/tcp  open  netbios-ssn  syn-ack
445/tcp  open  microsoft-ds syn-ack
3306/tcp open  mysql        syn-ack
5000/tcp open  upnp         syn-ack
6555/tcp open  unknown      syn-ack
8080/tcp open  http-proxy   syn-ack
9999/tcp open  abyss        syn-ack


# http://10.10.18.196/upload/

# http://10.10.18.196/betatest/
search /
```

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
tdurden:x:1000:1000:Tyler Durden:/home/tdurden:/bin/bash
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
narrator:x:1002:1002::/home/narrator:/bin/bash
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
nginx:x:997:994:Nginx web server:/var/lib/nginx:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
librenms:x:996:993::/opt/librenms:/bin/bash
librenms:x:996:993::/opt/librenms:/bin/bash

```
```bash
ssh narrator@ip

X8JEETQmf3hkS65f
```
# http://tyler.thm:8080/

admin:admin