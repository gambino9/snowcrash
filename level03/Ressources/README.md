At the beginning, we see a `level03` executable file. If we execute it, it displays
'Exploit me'

If we `file level03`, it outputs :
```
level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV),
dynamically linked (uses shared libs), for GNU/Linux 2.6.24,
BuildID[sha1]=0x3bee584f790153856e826e38544b9e80ac184b7b, not stripped
```
When an executable file is setuid, it runs as the user who owns the executable
file instead of the user who invoked the program. The letter s replaces the
letter x .

And we notice that the user of `level03` file is `flag03`. Which is the user we 
need to `su` in to get to the next level.

If we `strings level03` to print the strings of printable characters,  we notice
this peculiar input : `/usr/bin/env echo Exploit me`

`env` can print environment variables and also executes something in another
environment. For example, it will look over the PATH variable when looking
for a command to execute

Because `level03` contains the code `echo Exploit me` with the `flag03` privilege
and that we need to launch `getflag` under `flag03` permissions, we do the
following :

We `cd /tmp`, one of the few directory where we have permission to create a file. 
We create an 'echo' file `vi echo` and write `getflag` in it.

We make it executable `chmod +x echo`

We add `/tmp` to the PATH variable so when we execute `level03`, it will look all 
over PATH (and in /tmp) for an `echo` command to execute : `export PATH=/tmp:$PATH`

Now, if we `./level03` we get the flag to the next level !


# Sources :

What is 's' in linux file permissions and explanation of `setuid` and `setgid`
- https://www.sovereignvalley.com/what-is-the-s-in-linux-file-permissions/
- https://www.computerhope.com/jargon/s/setuid.htm

Ten ways to analyse binary files in Linux (`strings` command)
- https://opensource.com/article/20/4/linux-binary-analysis

What is PATH and how to add a new path to PATH environment variable :
- https://www.baeldung.com/linux/path-variable