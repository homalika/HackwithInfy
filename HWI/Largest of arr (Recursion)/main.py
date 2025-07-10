def large(index, arr, m):
    if index == len(arr):
        return m
    if arr[index] > m:
        m = arr[index]
    return large(index + 1, arr, m)

arr = [1, 7, 5, 4, 3, 2, 9]
m = 0
print(large(0, arr, m))