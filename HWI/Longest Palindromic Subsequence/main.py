# https://blog.algomaster.io/p/15-leetcode-patterns

s = "bbbab"
ss = s[::-1]
m = [[0]*(len(s)+1) for i in range(len(ss)+1)]
for i in range(len(s)-1, -1, -1):
    for j in range(len(ss)-1, -1, -1):
        if s[i] == ss[j]:
            m[i][j] = 1 + m[i+1][j+1]
        else:
            m[i][j] = max(m[i+1][j], m[i][j+1])
for i in m:
    print(i)
print("Length of longest palindromic subsequence is:", m[0][0])
i = 0
j = 0
res = ""
while i < len(s) and j < len(ss):
    if s[i] == ss[j]:
        res += s[i] # or res += ss[j]
        i += 1
        j += 1
    elif m[i][j+1] > m[i+1][j]:
        j += 1 
    else:
        i += 1
print(res)
    