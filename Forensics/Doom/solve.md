# Solution

There are 3 ways to solve this challenge.
1. Using unzip command
```
unzip doom.png
```
trying the above command in terminal will lead to a "flag.txt" file being created in the same directory as where you ran the command(ensure doom.png is also there in the given directory, else you will get errors). Opening flag.txt in any text editor will display the flag.
<br />

2. using strings command
```
strings doom.png | grep ZenseCTF
```
trying the above command in terminal will directly give you the flag in the terminal itself. grep essentially searches for any string in the output provided by strings command that has the substring mentioned - here, "ZenseCTF".
If we check the output by using strings doom.png > out.txt, we will see the flag [here](https://github.com/Nilsiloid/Zense-MiniCTF/blob/main/Forensics/Doom/strings_data.png)
<br />

3. using binwalk command
```
binwalk doom.png
binwalk -e doom.png(to extract)
```
binwalk command is used to see the file contents of a specified file. When we run binwalk on doom.png, we see a lot of hidden files. Thus, we will use the -e command to extract these hidden files. Upon running this command, a new directory called "_doom.png.extracted" will be formed containing flag.txt and a zip file. Opening flag.txt leads us to the flag.
<br />

The flag is:

```
ZenseCTF{5t3g_b3g1nn3r!}
```