arr = [2, 7, 11, 23, 8, 12]
mask = 0
xor = 0
for i in range(31, -1, -1):
    mask = mask | (1 << i)
    pre = {num & mask for num in arr}
    print("Prefixes: ", pre)
    temp = xor | (1 << i)
    for prefix in pre:
        if temp ^ prefix in pre:
            xor = temp
            break
print(xor)