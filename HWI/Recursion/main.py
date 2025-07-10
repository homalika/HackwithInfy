def fun1(n):
    if n == 11:
        return
    print(n)
    fun1(n + 1)
    print(n)
    
def fun2(n):
    if n == 11:
        print("Biryani")
        return
    print(n)
    fun2(n + 1)
    print(n)
    
def fun3(n):
    if n == 11:
        return "Biryani"
    print(n)
    b = fun3(n + 1)
    print(n)
    return b

print("\nFun1")
fun1(1)
print("\nFun2")
fun2(1)
print("\nFun3")
print(fun3(1))