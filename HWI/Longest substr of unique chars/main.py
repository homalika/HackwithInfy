MAX_CHAR = 26
s = 'geeksforgeeks'
if len(s) == 0 or len(s) == 1:
    print(len(s))
res = 0
vis = [False] * 26
l = 0
r = 0
while r < len(s):
    while vis[ord(s[r]) - ord('a')] == True:
        vis[ord(s[l]) - ord('a')] = False
        l += 1
        vis[ord(s[r]) - ord('a')] = True
        res = max(res, (r - l + 1))
        r += 1
print(res)