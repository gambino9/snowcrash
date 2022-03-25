In this level, we have a `setuid` executable file : `level13`.

`./level13`

>UID 2013 started us but we we expect 4242

To find all UIDs, we `cat /etc/passwd` : 

> level13:x:2013:2013::/home/user/level13:/bin/bash

What we need to do is to change the UID. After a few researches, we find out
it's probably not possible, and that it must be something else.

`nm level13` : 

> ...
> 08048450 t frame_dummy   
08048474 T ft_des   
         U getuid@@GLIBC_2.0   
0804858c T main   
         U printf@@GLIBC_2.0   
         U strdup@@GLIBC_2.0   


We use `gdb` to disassemble the program.

`gdb level13`

We put a breakpoint in the main, so we can understand how it works.

`br main`, and then we run the program : `r` :

```
(gdb) r
Starting program: /home/user/level13/level13 

Breakpoint 1, 0x0804858f in main ()
```

We use the `stepi` or `si` instruction, that steps one instruction exactly.

# Sources :