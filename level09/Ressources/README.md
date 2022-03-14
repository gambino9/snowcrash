In this level, we have a `setuid` script named `level09` and a data file `token`.
If we `strings` the file, we can find this sentence : `you should not reverse this`
The script requires one argument.

`./level09 "aaaaaaaa"`
>abcdefgh

We understand that the script does a Rot to each character depending on their
index in the string (index + 1).  
We also notice that if we `cat token` file : 
> f4kmm6p|=�p�n��DB�Du{��

We understand, because of the non-printable characters, that the `token` file
is the output of the `level09` algo on the original token. We simply need to
write a script that reverses the action of the `level09` script :
```
#!/usr/bin/python

import sys

def reverse_string(string):
    ret_string = ""
    for i, char in enumerate(string):
        ret_string += chr((ord(char) - i))
    return ret_string

s = sys.argv[1]
print(reverse_string(s))
```

We put the script in `/tmp` and we execute it this way :   
`python /tmp/test2.py $(cat token)`

> f3iji1ju5yuevaus41q1afiuq

This happens to be the correct password for `su flag09`. When we `getflag` :

> Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z

