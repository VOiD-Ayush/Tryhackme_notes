#!/bin/bash

cp b64.txt test.txt
echo "[-] Making a test file to work."
echo "[-] Decoding "
for i in {1..50}
do  
	echo `base64 -d test.txt` > test.txt
done

echo -n "[-] Here is the decoded txt : "
cat test.txt