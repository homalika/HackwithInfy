arr = [3, 1, 2, 2, 3, 2, 3]
ones = 0
twos = 0
for i in arr:
    ones = (ones ^ i) & ~twos
    twos = (twos ^ i) & ~ones
print(ones)