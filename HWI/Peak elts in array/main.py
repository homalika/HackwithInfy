arr = [1, 2, 3, 8, 6, 7]
n = len(arr)
'''
for i in range(1, n - 2):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(arr[i])
'''
if n == 1:
    print(0)
elif arr[0] > arr[1]:
    print(0)
elif arr[n - 1] > arr[n - 2]:
    print(n - 1)
l = 1
r = n - 2
while l <= r:
    mid = (l + r) // 2
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        print(mid)
        break
    elif arr[mid] > arr[mid - 1]:
        l = mid + 1 
    else:
        r = mid - 1 