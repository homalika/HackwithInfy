arr = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
k = 2
count = 0
start = 0
maxlen = 0
for i in range(len(arr)):
    if arr[i] == 0:
        count += 1
    while count > k:
        if arr[start] == 0:
            count -= 1
        start += 1
    maxlen = max(i - start + 1, maxlen)
print(f"Max consecutive 1's in a binary array with at most {k} flips: ", maxlen)