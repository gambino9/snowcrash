In this level, there is nothing. We try to `getflag` : 

> level14@SnowCrash:~$ getflag  
Check flag.Here is your token :   
Nope there is no token here for you sorry. Try again :) 

We look for getflag in order to exploit the binary : 

```
level14@SnowCrash:~$ find / -name getflag 2>/dev/null 
/bin/getflag
/rofs/bin/getflag
```

We go to `/bin` and then we `gdb` getflag binary.

First, we notice that if we run the program inside `gdb`, the output is not
the same :   
```
(gdb) r
Starting program: /bin/getflag 
You should not reverse this
[Inferior 1 (process 3408) exited with code 01]
```

This is going to be explained in a little while.


We know that in order to get a flag from getflag, just like the previous level
we have to give the correct `uid`. But if we try the same technique as in
level13, it doesn't work.

If we disassemble the `main` and look closely, just tight after the call to
`getuid`we notice that some operations are repeated several time :

```
0x08048afd <+439>:	call   0x80484b0 <getuid@plt>
   0x08048b02 <+444>:	mov    %eax,0x18(%esp)
   0x08048b06 <+448>:	mov    0x18(%esp),%eax
   0x08048b0a <+452>:	cmp    $0xbbe,%eax
   0x08048b0f <+457>:	je     0x8048ccb <main+901>
   0x08048b15 <+463>:	cmp    $0xbbe,%eax
   0x08048b1a <+468>:	ja     0x8048b68 <main+546>
   0x08048b1c <+470>:	cmp    $0xbba,%eax
   0x08048b21 <+475>:	je     0x8048c3b <main+757>
   0x08048b27 <+481>:	cmp    $0xbba,%eax
   0x08048b2c <+486>:	ja     0x8048b4d <main+519>
   0x08048b2e <+488>:	cmp    $0xbb8,%eax
   0x08048b33 <+493>:	je     0x8048bf3 <main+685>
   0x08048b39 <+499>:	cmp    $0xbb8,%eax
   0x08048b3e <+504>:	ja     0x8048c17 <main+721>
   0x08048b44 <+510>:	test   %eax,%eax
   0x08048b46 <+512>:	je     0x8048bc6 <main+640>
   0x08048b48 <+514>:	jmp    0x8048e06 <main+1216>
   0x08048b4d <+519>:	cmp    $0xbbc,%eax
   0x08048b52 <+524>:	je     0x8048c83 <main+829>
   0x08048b58 <+530>:	cmp    $0xbbc,%eax
   0x08048b5d <+535>:	ja     0x8048ca7 <main+865>
   0x08048b63 <+541>:	jmp    0x8048c5f <main+793>
   0x08048b68 <+546>:	cmp    $0xbc2,%eax
   0x08048b6d <+551>:	je     0x8048d5b <main+1045>
   0x08048b73 <+557>:	cmp    $0xbc2,%eax
   0x08048b78 <+562>:	ja     0x8048b95 <main+591>
   0x08048b7a <+564>:	cmp    $0xbc0,%eax
   0x08048b7f <+569>:	je     0x8048d13 <main+973>
   0x08048b85 <+575>:	cmp    $0xbc0,%eax
   0x08048b8a <+580>:	ja     0x8048d37 <main+1009>
   0x08048b90 <+586>:	jmp    0x8048cef <main+937>
   0x08048b95 <+591>:	cmp    $0xbc4,%eax
   0x08048b9a <+596>:	je     0x8048da3 <main+1117>
   0x08048ba0 <+602>:	cmp    $0xbc4,%eax
   0x08048ba5 <+607>:	jb     0x8048d7f <main+1081>
   0x08048bab <+613>:	cmp    $0xbc5,%eax
   0x08048bb0 <+618>:	je     0x8048dc4 <main+1150>
   0x08048bb6 <+624>:	cmp    $0xbc6,%eax
   0x08048bbb <+629>:	je     0x8048de5 <main+1183>
   0x08048bc1 <+635>:	jmp    0x8048e06 <main+1216>
```

Unfortunately, if we try to change the value of `eax` right after the call of
`getuid` by putting a breakpoint, the program have the same output.

We try to understand why the `getflag` program does not have his usual output.


Several times, a comparison is made between `eax` register and a hexadecimal
value. Those values, converted, are ranged between 3000 and 3014. We understand
that the return value of `getuid` is assigned to `eax` register, and compared
to many values several times until one of them matches. In order to have this
flag, our UID is supposed to be 3014.

But if we try to assign to `eax` the value 3014, the program still doesn't give
us any flag.

As we keep looking at the main disassembly, we notice a call to `ptrace`
function. The `ptrace` system call allows one process to trace another. But
only one process can trace another, if a second process tries to attach with
ptrace then the second ptrace will fail, returning -1.

What we should do here, is putting a breakpoint right after the call to `ptrace`
and set `eax` variable to `0`, so we can bypass `ptrace` error.

>(gdb) br *0x08048b02   
Breakpoint 1 at 0x8048b02

> (gdb) set var $eax=0

Now the `getflag` function works just fine, but there is no flag for us yet.

Changing the value of `eax` here is only to prevent `ptrace` to return -1, but
we still need to change the value of the UID to 3014 :   
`br *0x08048b02`. We put a breakpoint right after the call to `getuid` function,
where the return value of `getuid` is assigned to `eax`.

Now we have 2 breakpoints : 
```
(gdb) i br
Num     Type           Disp Enb Address    What
4       breakpoint     keep y   0x08048b02 <main+444>
5       breakpoint     keep y   0x0804898e <main+72>
	breakpoint already hit 1 time
```


Then, when we start to run, we `jump` into this breakpoint and change the value
of `eax` : `set var $eax=3014`. And then, if we `next` : 

```
(gdb) next
Single stepping until exit from function main,
which has no line number information.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
```


# Sources :

About `ptrace` : 
- https://stackoverflow.com/questions/33646927/bypassing-ptrace-in-gdb#33647443
- https://www.bases-hacking.org/ptrace.html
