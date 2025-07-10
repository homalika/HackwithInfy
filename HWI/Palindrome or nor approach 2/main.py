s = 'Gee@ke$@eG'
l = 0
r = len(s) - 1
found = True
while l <= r:
    if s[l].isalnum() and s[r].isalnum():
        if s[l] == s[r]:
            l += 1 
            r -= 1 
        else:
            found = False
            break 
    elif s[l].isalnum() and not s[r].isalnum():
        r -= 1 
    elif not s[l].isalnum() and s[r].isalnum():
        l += 1 
    else:
        l += 1 
        r -= 1 
if found:
    print("Palindrome")
else:
    print("Not Palindrome")