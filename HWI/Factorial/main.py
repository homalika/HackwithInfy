def fun(n):
    if n == 1:
        return 1 
    return n * fun(n - 1)
    
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("Factorial of 5: ")
print(fun(5))

print("Fibonacci of 5: ")
print(fib(5))