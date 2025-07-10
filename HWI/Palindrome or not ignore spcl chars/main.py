s = 'Gee@ke$@eG'
l = 0
r = len(s) - 1
found = True
while l <= r:
    if not s[l].isalnum():
        l += 1 
        continue
    if not s[r].isalnum():
        r -= 1 
        continue
    if s[l] != s[r]:
        found = False
        break 
    l += 1
    r -= 1 
if found:
    print("Palindrome")
else:
    print("Not Palindrome")