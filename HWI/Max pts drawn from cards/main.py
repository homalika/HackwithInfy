arr = [1, 8, 4, 2, 4, 6, 3, 2]
k = 3 # take 3 values from arr either left most or right most consecutive
# using sliding window
sums = 0
start = 0
for i in range(k):
    sums += arr[i]
maxx = sums
count = 1
while k - count >= 0:
        sums = sums - arr[k - count] + arr[-count]
        maxx = max(sums, maxx)
        count += 1
print(maxx)