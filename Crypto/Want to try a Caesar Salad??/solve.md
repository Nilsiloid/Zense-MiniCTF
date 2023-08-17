# Solution

The challenge description gives us a link that leads to Zense's official Instagram page. Now, this CTF was held after an "Introduction to CTF" session. There's only 2 posts in relation to an introductory session and in the comment section of the older post, you will see the following message.

```
Is this relevant to my CTF session??

WbkpbZQC{t45_qe1p_Gri1r5_Z4b5xop_z1me3o???}
```
<br />

Now, the question mentions Caesar salads, thus giving a hint to check for Caesar cipher since the text mentioned is obviously encrypted. Upon searching for an online decoder, you will find [this](https://www.dcode.fr/caesar-cipher). Inputting the given cipher text here and decrypting via brute force will give you the flag.
<br />

The flag is:

```
ZenseCTF{w45_th1s_Jul1u5_C4e5ars_c1ph3r???}
```