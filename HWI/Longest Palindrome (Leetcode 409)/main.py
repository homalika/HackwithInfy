def longestPalindrome(s):
    q = set(s)
    c = 0
    odd = False
    for i in q:
        if s.count(i)%2 == 0:
            c += s.count(i)
        else:
            c += s.count(i) - 1 
            odd = True
    if odd:
        return c + 1
    else:
        return c 

print(longestPalindrome("abccccdd"))
