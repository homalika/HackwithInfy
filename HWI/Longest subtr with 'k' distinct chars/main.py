s = 'abcbbddcb'
k = 2 # output = 4
d = {}
start = 0
maxlen = 0
for i in range(len(s)):
    d[s[i]] = d.get(s[i], 0) + 1 
    while len(d) > k:
        d[s[start]] -= 1 # reducing frequency
        if d[s[start]] == 0:
            del d[s[start]]
        start += 1
    if len(d ) == k:
        maxlen = max(i - start + 1, maxlen)
print(f"Max length of chars with {k} distinct characters: ", maxlen)