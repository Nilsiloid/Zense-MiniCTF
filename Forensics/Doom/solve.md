# Solution

Pay close attention to the challenge name. E-X-I-F is highlighted. This points to exiftool, a tool used for reading, writing and manipulating image, audio, video and PDF metadata. Using exiftool on the png image provided in the challenge would lead to a weird encoding of some sort in the Creator entity.
<br />

Upon seeing it, it looked to be of Base64 encoding, which in fact is pointed to in the challenge description where it says Messi spent 64 minutes encoding this in his BASEment. Thus, upon decoding it using Base64 decoder, we get the flag.
<br />

The flag is:

```
ZenseCTF{Me5sI_I5_th3_g04t}
```