arr = [2, 3, 3, 3, 4]
k = 3
l = 0
fo = -1
r = len(arr) - 1 
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == k:
        fo = mid
        r = mid - 1
    elif arr[mid] < k:
        l = mid + 1
    else:
        r = mid - 1 
print("Position of first occurrence: ", fo)