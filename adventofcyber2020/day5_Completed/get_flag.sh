#!/bin/bash

echo -n "admin password is "  
cat sql.log| grep admin | tr '|' '\b' | cut -d ' ' -f 2
echo -n "flag is "
cat sql.log| grep thm | tr '|' '\b'