'''
# using Recursion
c = 0
def fun(n):
    global c
    c += 1
    if n <= 1:
        return n 
    else:
        return fun(n - 1) + fun(n - 2)
print(fun(10))
print(c) # prints number of recursive calls 
'''
c = 0
def fun(n, memo):
    global c
    if memo[n] != -1:
        return memo[n]
    c += 1
    if n <= 1:
        memo[n] = n
        return n 
    else:
        memo[n] = fun(n - 1, memo) + fun(n - 2, memo)
        return memo[n]
n = 10
memo = [-1]*(n+1)
print(fun(n, memo))
print(c)
