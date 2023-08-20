# Solution

In the given challenge description, we are given 2 files - 'chall.py' and 'output.txt'. The output given from running the algorithm on the flag is given in the output.txt file. As is obvious, the participant should use the output to reverse it by reversing the algorithm.
In the python script, the algorithm used on the flag string is as follows:
```
Every even index gets added with 1 while every odd index gets subtracted with 1.
```

Now, we need to reverse this algorithm which would just be the following:
```
subtract 1 at even index and add 1 at odd index.
```
<br />

This has been done using the following python script - [solve.py](https://github.com/Nilsiloid/Zense-MiniCTF/blob/main/Rev/Flag%20Extraction%3F%3F/solve.py)

The flag is:
```
ZenseCTF{r3v_0r1g1n5}
```