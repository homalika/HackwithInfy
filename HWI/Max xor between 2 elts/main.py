arr = [2, 7, 11, 23, 8, 12]
xor = 0
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        xor = max(xor, arr[i] ^ arr[j])
print(xor)