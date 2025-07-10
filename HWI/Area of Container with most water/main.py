arr = [2, 8, 3, 5, 7, 6, 4]
area = 0
l = 0
r = len(arr) - 1
while l < r:
    area = max(area, (r - l) * min(arr[l], arr[r])) #(r-l) is width
    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1
print("Max area is: ",area)