There is nothing in level01, so we check how to find a password in Linux system

We have to `cat /etc/passwd` and we notice in the output the following entry : 

`flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash`

We copy this file into our local system

`scp -P 4242 level01@192.168.0.18:/etc/passwd .`

Install john the ripper

`sudo apt-get install john -y`

`echo flag01:42hDRfypTqqn > crack` copy encrypted password in a file

Use john the ripper on `crack` file

`john crack --show`

output : 

`flag01:abcdefg`

The passphrase `abcdefg` happens to be the correct password to `su floag01` command

# Sources :

https://www.geeksforgeeks.org/understanding-the-etc-passwd-file/

https://www.freecodecamp.org/news/scp-linux-command-example-how-to-ssh-file-transfer-from-remote-to-local/

https://linuxhint.com/john_ripper_ubuntu/

