# Solution

In the given challenge description, we are given an image - called brand_image.png. The title "hexing into images 101" also gives us a clue about looking at the hex data of the given image.
<br />

The hex data can be looked at using a simple hex editor, such as gedit, hexedit, ghex and so on or by looking at the output generated on running the strings command followed by the image name.
```
strings brand_image.png > out.txt
hexedit brand_image.png
```

Either of the above two commands will lead us to solving the challenge.
If you run the strings command, you will notice this very weird statement on the 6th line - V3G_BXRIYANI_MATT3RS, followed by ZENSE on the 9th line. This is in fact our answer!
If you run the hexedit command, you will see the following in your terminal - [hex_data.png](l.com). Here you can notice the words Zense and just above it V3G_BXRIYANI_MATT3RS. This leads us to believe that V3G_BXRIYANI_MATT3RS is the true artist name of CRABBY and we are in fact correct!
<br />

The flag is:

```
ZENSE{V3G_BXRIYANI_MATT3RS}
```