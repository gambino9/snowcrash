In this level, we have 2 files. A php script `level06.php` and a `level06` file
that is also a `setuid` with the `flag06` permissions. `level06` is probably the
compiled version of `level06.php` file.

If we try to `./level06` we get an error message. Let's take a look at the php script : 
```
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```

Let's make it more visible : 

```
#!/usr/bin/php
<?php
function y($m)
{
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}

function x($y, $z)
{
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}

$r = x($argv[1], $argv[2]);;
print $r;
?>
```

In the 5th line `$m = preg_replace("/\./", " x ", $m);`, the preg_replace
function replaces `/\./` pattern in the string `$m` by ` x `.

In line 12 `$a = file_get_contents($y);`, the argument `y` is assigned to the
variable `a`, and this argument is supposed to be a file, or else it is going
to raise an error.

The 13th line `$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);` is the
most important to understand. The `e` modifier is a deprecated regex modifier
which allows you to use PHP code within your regular expression. This means
that whatever you parse in will be evaluated as a part of your program. 

So, what we need to do is to pass the command `getflag` contained in a file 
as the first argument of the php script. The way to pass a system command to php
is by using the `system` php command. 

So we create `/tmp/test` where we put the following content : `[x {${system(getflag)}}]`
Which gives us the token to the next level !

# Sources :

About the deprecated `/e` modifier` :
- https://stackoverflow.com/questions/16986331/can-someone-explain-the-e-regex-modifier

About the `system` php command : 
- https://www.php.net/manual/fr/function.system.php
