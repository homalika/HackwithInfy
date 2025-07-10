def query(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res
    
def ran(tree, l, r):
    return query(tree, r) - query(tree, l - 1)
    
def update(tree, i, delta):
    n = len(tree)
    while i < n:
        tree[i] += delta
        i += (i & -i)
        
def build(arr, tree):
    n = len(arr)
    for i in range(1, n):
        update(tree, i, arr[i])
        
        
arr = [0, 1, 2, 3, 4, 5, 6]
print(arr)
tree = [0] * len(arr)
build(arr, tree)
print(tree)
print(ran(tree, 3, 6))
