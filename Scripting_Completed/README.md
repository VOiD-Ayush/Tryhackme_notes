# Scripting 

> VOiD | Tuesday 03 August 2021 01:43:54 PM IST

My IP : 10.17.6.109
Target IP : 



# [1] Task 1
write a shell/python script to get the flag

flag is HackBack2019=


# [2] Task 2

You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0.

The format is: operation, number, next port.

For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.

Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499

Do this until you the page response is STOP (or you hit port 9765).

Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again...

Go to: http://<machines_ip>:3010 to start...

General Approach(it's best to do this using the sockets library in Python):

Create a socket in Python using the sockets library
Connect to the port 
Send an operation
View response and continue

answer
> 344769.12




