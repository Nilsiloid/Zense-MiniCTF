# Solution

The question points to injections of some sorts - the most famous one in Web Exploitation challenges is SQL Injections. One of the most helpful repositories for SQL Injection payloads is [this](https://github.com/payloadbox/sql-injection-payload-list) and from this github repo, if we navigate to generic SQL Injection payloads, we will find some general SQLi payloads that we can use.
<br />

Now, upon opening the website, we see a basic page asking for an input. Trying "admin" doesn't work and it displays an error.
Thus, we can clearly understand the website wants us to payload it via SQLi. Thus trying "' OR 1=1 --" leads us to a page that displays the flag in plaintext.
<br />

The flag is:

```
ZenseCTF{5QLi-f0r-fun!}
```