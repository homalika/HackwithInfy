arr = [2, 3, 5, 7, 4]
tar = 12
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == tar:
            a, b = arr[i], arr[j] 
print(a, b)