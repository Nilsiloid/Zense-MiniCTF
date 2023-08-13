# Solution

Upon Googling "What part of the website could tell you where the creator doesn't want you to look?", we see the mention of a robots.txt file. This tells search engines crawlers which URLs the crawler can access on your site.

Now, the obvious thing to look at is the url of the CTF with /robots.txt at the end of it.
Thus, upon checking http://ctf.iiitb.net/robots.txt we find the flag clearly displayed there.

```
Flag - ZenseCTF{r0bot5_ar3_c0oL}
```