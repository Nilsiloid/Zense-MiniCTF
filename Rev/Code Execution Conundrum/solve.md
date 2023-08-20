# Solution

In the given challenge description, we are given an executable file 'hello'. Now, the most basic way to run such executable files is to use the chmod command. We can give the most basic requirements to run the executable by using the following:
```
chmod +x hello
```

This gives the user permissions to run the executable and by using './hello', we are able to run the executable which incidentally directly prints the flag.
```
./hello
```
<br />

The flag is:
```
ZENSE{WHO_IS_COMPILER_WHY_IS_ASSEMBLER}
```