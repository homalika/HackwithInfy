print("Enter n: ")
n = int(input())
if bin(n).count('1') == 1:
    print("n is power of 2")
else:
    print("n is not power of 2")