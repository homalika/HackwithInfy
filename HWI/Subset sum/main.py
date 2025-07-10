def fun(arr, n, target):
    if target == 0:
        return True
    if n <= 0:
        return False
    if arr[n - 1] > target:
        return fun(arr, n - 1, target)
    return fun(arr, n - 1, target) or fun(arr, n - 1, target - arr[n - 1])

arr = [3, 4, 5, 6, 8]
target = 7
n = len(arr)
print(fun(arr, n, target))