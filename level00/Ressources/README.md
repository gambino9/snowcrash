This command gets files that are executable by user flag00 | redirecting stderr (file descriptor 2) over to /dev/null to discard it  

`find / -user flag00 -perm -000 2>/dev/null`

The file is `/usr/sbin/john`

When you cat the file, you get this :
`cdiiddwpgswtgt`

This string is not accepted as the password of `su flag00` so it gotta be something else

We can try by going on the following website : https://www.dcode.fr/

By trying a ROT decoding, and by changing the number (2), we get the following passphrase : `nottoohardhere`

This passphrase is accepted as psswd for `su flag00`

# Sources :

https://stackoverflow.com/questions/15247563/how-can-i-find-files-that-only-have-certain-permission-for-owner

https://unix.stackexchange.com/questions/82515/how-can-i-filter-those-permission-denied-from-find-output

https://www.dcode.fr/