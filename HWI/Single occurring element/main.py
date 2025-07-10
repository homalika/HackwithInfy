arr = [1, 2, 3, 1, 3]
xor = 0
for i in range(len(arr)):
    xor = xor ^ arr[i]
    #(((1^2)^3)^1)^3
    #1^1 = 0 and 3^3 = 0 -- we get 0^2^0 = 2
print(xor) # single occurring element