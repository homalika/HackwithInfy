def max_val(arr):
    maxi = -1
    for i in arr:
        if i > maxi:
            maxi = i
        else:
            pass
    return maxi
    
def tot_hrs(arr, cap):
    tot = 0
    for i in arr:
        tot += (i + cap - 1) // cap
    return tot
    
def min_cap(arr, hrs):
    # binary search
    l = 1 
    r = max_val(arr)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if tot_hrs(arr, mid) <= hrs:
            ans = mid
            r = mid - 1 
        else:
            l = mid + 1 
    return ans
    
arr = list(map(int, input().split()))
h = int(input())
res = min_cap(arr, h)
print(res)