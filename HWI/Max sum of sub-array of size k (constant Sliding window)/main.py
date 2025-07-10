arr = list(map(int, input("Enter list of elements: ").split()))
k = int(input("Enter window-size: "))
start = 0 
sums = 0
maxx = 0
for i in range(len(arr)):
    sums += arr[i]
    if i - start + 1 == k:
        maxx = max(sums, maxx)
        sums -= arr[start]
        start += 1
print(f"Maximum sum of sub-array of window-size {k}:", maxx)