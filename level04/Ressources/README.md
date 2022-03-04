In this level, we have the following `setuid` Perl script :
```
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

As a setuid script, it executes with the `flag04` permissions, which is the
permissions we need to execute `getflag` in order to get to the next level.

Let's explain the script.

`# localhost:4747` means something is going on port 4747. Let's get to this url
using the IP address of the VM : `http://192.168.0.18:4747`

This line `use CGI qw{param};` indicates us the the script is gonna use `param`
function from CGI library. 

A CGI is simply a program that is called by the webserver, in response to some
action by a web visitor. And if you're writing a CGI that's going to generate
an HTML page, you must include this statement somewhere in the program before
you print out anything else: `print "Content-type: text/html\n\n";`. Which is
present in `level04` script.

The `param` function from CGI allows us to pass arguments to a URL with a
question mark followed by a `key=value` the value being the value we
want to get.

The rest of the script is a function `x` and a call to this function.
`x` assign the argument at the index 0 of the `$_` scalar variable to `y`. Then
it is gonna echo `y` and redirect error messages. The function is then called
with the `"x"` argument.

Since the script is a `setuid`, we need to pass the `getflag` command as an
argument to the URL. But like the previous flag, the `echo` command is a problem.

If we look online, we can see that we can `echo` the output of a command after
executing it by doing this : `echo $(<your_command_here>)`.

We rewrite the URL by passing `"x"` argument as a key like this :
`192.168.0.18:4747/?x=$(getflag)`

This output the flag that get us to the next level !


# Sources :

Perl programming language :
- https://fr.wikipedia.org/wiki/Perl_(langage)

Some basic and information about CGI programming with Perl :
- http://www.cgi101.com/book/ch1/text.html

Explaining the `param` function :
- https://www.cs.ait.ac.th/~on/O/oreilly/perl/learn32/ch18_04.htm