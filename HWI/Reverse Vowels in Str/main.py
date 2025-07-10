s = 'icecream'
def reverseVowels(s):
    def isVowel(c):
        if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
            return True
        return False
    res = []
    for i in s:
        if isVowel(i):
            res.append(i)
    ress = res[::-1]
    k = ''
    j = 0
    for i in range(len(s)):
        if isVowel(s[i]):
            k += ress[j]
            j += 1
        else:
            k += s[i]
    return k
print(reverseVowels(s))