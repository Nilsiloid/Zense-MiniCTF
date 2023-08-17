# Solution

The challenge description gives us a file that has the following:
```
Vm0wd2VHUXhUblJXYTJSWVYwZDRWMWxyWkc5V2JGbDNXa1JTV0ZKdGVGWlZiWFF3VjB
aS2MxZHVjRmROYWxab1ZrZHplRmRHVm5OaVJsWlhZa1p3ZVZkWGRHdFRNVTVYVW01T1
dHSkhVazlXYlhSM1VsWmFjVkpzV214U01EVllWbTAxUjFkSFNrbFJiazVhVjBoQ1dGW
nJXbXRqTVhCRlZXMTBUbFpYZDNwV1JFWmhZekZXZEZKcVdtbFNiV2hoVm01d1IyTnNV
bFZTYlhSWVVsUkdTbGRyVlRGVk1ERldWMVJHVjJKVVJUQlpha3BIVmpGU2NscEdhR2x
TVlhCWlYxZDRiMUV5VW5OVmJsSnNVbXR3Y2xSV2FFTlRWbFowVFZSU2FGWnJOVWRWTW
5SclZqQXhkVlZ1V2xoV2JIQllWV3BHZDFKc1duTlRiR1JUVFRBd01RPT0=
```

Now, on first glance, this seems like Base64 encoding. We can then use an online Base64 decoder to decode this ciphertext. Using [this](https://www.base64decode.org/) we can decode the given ciphertext. But in the first try, we will not get any decrypted/decoded flag.
<br />

Now, the question title is "Repetitions", could this mean multiple Base64 encryptions?? Trying to decode the decrypted text in each iteration, we do obtain the flag after 5-6 repetitions.
<br />

The flag is:

```
ZenseCTF{base64_n3st3d_i5_4nn0yin5_38fsd7o9}
```