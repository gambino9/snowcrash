In this level, we have a `setuid` executable file : `level13`.

`./level13`

>UID 2013 started us but we we expect 4242

To find all UIDs, we `cat /etc/passwd` : 

> level13:x:2013:2013::/home/user/level13:/bin/bash

UID 2013 is the UID of level13 user.   
What we need to do is to change the UID to 4242. After a few researches, we find out
it's probably not possible, and that it must be something else.

We use `gdb` : `gdb level13`

Let's take a look at the disassembly of the main of the executable : `disas main` : 

> (gdb) disas main   
Dump of assembler code for function main:   
   0x0804858c <+0>:	push   %ebp   
   0x0804858d <+1>:	mov    %esp,%ebp   
   0x0804858f <+3>:	and    $0xfffffff0,%esp   
   0x08048592 <+6>:	sub    $0x10,%esp   
   0x08048595 <+9>:	call   0x8048380 <getuid@plt>   
   0x0804859a <+14>:	cmp    $0x1092,%eax   
   0x0804859f <+19>:	je     0x80485cb <main+63>   
   0x080485a1 <+21>:	call   0x8048380 <getuid@plt>   
   0x080485a6 <+26>:	mov    $0x80486c8,%edx   
   0x080485ab <+31>:	movl   $0x1092,0x8(%esp)   
   0x080485b3 <+39>:	mov    %eax,0x4(%esp)   
   0x080485b7 <+43>:	mov    %edx,(%esp)   
   0x080485ba <+46>:	call   0x8048360 <printf@plt>   
   0x080485bf <+51>:	movl   $0x1,(%esp)   
   0x080485c6 <+58>:	call   0x80483a0 <exit@plt>   
   0x080485cb <+63>:	movl   $0x80486ef,(%esp)   
   0x080485d2 <+70>:	call   0x8048474 <ft_des>   
   0x080485d7 <+75>:	mov    $0x8048709,%edx   
   0x080485dc <+80>:	mov    %eax,0x4(%esp)   
   0x080485e0 <+84>:	mov    %edx,(%esp)   
   0x080485e3 <+87>:	call   0x8048360 <printf@plt>   
   0x080485e8 <+92>:	leave     
   0x080485e9 <+93>:	ret       
End of assembler dump.   

We can see that a call to `getuid` function is made at address `0x08048595`

Let's put a breakpoint on this function :

> (gdb) br *0x08048595   
Breakpoint 1 at 0x8048595

What we are going to do now is to literally step into `getuid` function in order
to return an integer `4242`. The following commands allow us to do this :

```
(gdb) br *0x08048595
Breakpoint 1 at 0x8048595
(gdb) r
Starting program: /home/user/level13/level13 

Breakpoint 1, 0x08048595 in main ()
(gdb) si
0x08048380 in getuid@plt ()
(gdb) return (int)4242
Make selected stack frame return now? (y or n) y
#0  0x0804859a in main
    ()
(gdb) n
Single stepping until exit from function main,
which has no line number information.
your token is 2A31L79asukciNyi8uppkEuSx
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6

```

Here we got our flag !


# Sources :