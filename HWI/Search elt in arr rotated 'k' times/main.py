arr = [1, 2, 3, 4, 5, 9]
k = 2  # rotate k times
tar = 4  
rarr = arr[-k:] + arr[:-k]
print(rarr)
l = 0
r = len(rarr) - 1 
found = -1
while l <= r:
    mid = (l + r) // 2
    if rarr[mid] == tar:
        found = mid
        break
    elif rarr[l] < arr[mid]:
        if tar >= rarr[l] and tar <= rarr[mid]:
            r = mid - 1
        else:
            l = mid + 1 
    elif arr[mid] < arr[r]:
        if tar >= rarr[mid] and tar <= rarr[r]:
            l = mid + 1
        else:
            r = mid - 1 
print("Element found at: ", found)