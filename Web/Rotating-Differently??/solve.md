# Solution

In the html file of the website, there is the following message.
<br />
```
 <!-- This might be of interest to you! -->
    <!-- AVMHV{NLFIRMSL_LK} -->
```

Upon seeing this, we can quickly notice that it is the flag but we have yet to decode it. We can decode it by noticing a few characters at the start itself. We know the first 5 letters correspond to ZENSE. Therefore, we can conclude that A -> Z, V -> E, M -> N and H -> S.
<br />

Taking some time to figure out a logic, we can realize that the letters are equidistant from their corresponding end. A is the 1st letter from the start, Z is the 1st from the end. Similarly, E is the 5th from the start whereas V is the 5th from the end and so on. Thus, upon writing a simple Python script [solve.py](https://github.com/Nilsiloid/Zense-MiniCTF/blob/main/Web/Rotating-Differently%3F%3F/solve.py) to evaluate this, we can obtain the flag.
<br />

The flag is:

```
ZENSE{MOURINHO_OP}
```