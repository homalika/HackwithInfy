# unlimited coins
n = [4, 5, 10]
tar = 7
a = [False]*(tar+1)
a[0] = True
for i in n:
    for j in range(i, tar + 1):
        if a[j - i]:
            a[j] = True
print(a)
print(a[tar])
# n = [2, 5, 10] -- target = 3 --> gives False