When we're connected to level05, we get notified that we have received an email.

We check where we can read any mail : `find / -name mail 2>/dev/null`.
We can see that `/var/mail` that a script named `level05` is here. It contains the following script :

`*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05`

The first part is a Cron tab that executes the script every 2 minutes.
It executes the script `/usr/sbin/openarenaserver`.

Here is the content of the `openarena` script : 

```
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

In a nutshell, this script iterates over every file located in
`/opt/openarenaserver/` directory, executes it, and then deletes it. And this happens
every 2 minutes.
When we `ls -l /usr/sbin/openarenaserver`, we also notice that it executes
itself with the `flag05` permissions. 

So what we need to do, is for this script to execute a script that contains
the `getflag` command. Since it deletes a script after executing it, we need to
redirect the `getflag` command elsewhere to gather the output.

So, in `/opt/openarena/` directory, we create a script where we write
`/bin/getflag >/opt/openarenaserver/test_directory/test_text` in a directory.

We just wait for 2 minutes for the script to executes our  `getflag` script ,
and we gather the output : `Check flag.Here is your token : viuaaale9huek52boumoomioc`

This happens to be the correct token for the next level.


# Sources :

What is the "+" sign in permissions in Linux
- https://www.golinuxhub.com/2013/12/what-is-plus-sign-in-permission-in-linux/

Basics of crontab : 
- https://www.hostinger.fr/tutoriels/cron-job/