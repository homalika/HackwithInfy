n = [1, 2, 5] # limited coins (1 each)
tar = 11  # tar = 8 -- gives True
a = [False]*(tar+1)
a[0] = True
for i in n:
    for j in range(tar, i - 1, -1): # to run till i each time we wrote (i - 1)
        if a[j - i]:
            a[j] = True
print(a)
print(a[-1]) # or print(a[tar])