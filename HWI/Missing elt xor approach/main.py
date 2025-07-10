arr = [0, 1, 3, 2, 5]
xor = 0
for i in range(len(arr)+1):
    xor = xor ^ i 
for i in arr:
    xor = xor ^ i 
print(xor)