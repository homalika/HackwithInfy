arr = [2, 3, 4, 5, 7]
target = 12
found = False
l = 0
r = len(arr) - 1 
while l < r:  # if l = r case must break
    if arr[l] + arr[r] == target:
        found = True
        break
    elif arr[l] + arr[r] < target:
        l += 1 
    else:
        r -= 1 
if found:
    print("Target found")
    print("Indices are: ", l, r)
else:
    print("Target not found")