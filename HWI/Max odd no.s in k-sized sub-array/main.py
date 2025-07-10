arr = [1, 3, 2, 9, 4, 7, 9]
k = 5 # output = 3
count = 0
start = 0
maxx = 0
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        count += 1
    if i - start + 1 == k:
        maxx = max(count, maxx)
        if arr[start] & 1 == 1:
            count -= 1
        start += 1
print(f"Max odd numbers in a {k} sized sub-array: ", maxx)