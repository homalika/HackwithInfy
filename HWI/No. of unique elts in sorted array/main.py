arr = [1, 2, 2, 3, 3, 4, 5, 5]
'''
arr1 = set(arr)
print(len(arr1))
'''
uni = []
for i in arr:
    if i not in uni:
        uni.append(i)
print(len(uni)) 
# approach 2 -- incomplete (error)
a = 0
for b in range(1, len(arr)):
    if arr[a] != arr[b]:
        a += 1 
        arr[a] = arr[b]
print(a)