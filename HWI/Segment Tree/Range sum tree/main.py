def build(arr, tree, n, start, end):
    if start == end:
        tree[n] = arr[start] # or tree[n] = arr[end]
        return
    else:
        mid = (start + end) // 2
        build(arr, tree, 2*n+1, start, mid)
        build(arr, tree, 2*n+2, mid + 1, end)
        tree[n] = tree[2*n+1] + tree[2*n+2]
        
def query(tree, node, s, e, l, r):
    if l > e or r < s:
        return 0
    elif l <= s and r >= e:
        return tree[node]
    else:
        mid = (s + e) // 2
        left = query(tree, 2*node+1, s, mid, l, r)
        right = query(tree, 2*node+2, mid + 1, e, l, r)
        return left + right

def update(arr, tree, node, s, e, ind, val):
    if s == e:
        arr[ind] = val
        tree[node] = val
        return
    else:
        mid = (s + e) // 2
        if i <= mid:
            update(arr, tree, 2*node+1, s, mid, ind, val)
        else:
            update(arr, tree, 2*node+2, mid + 1, e, ind, val)
        tree[node] = tree[2*node+1] + tree[2*node+2]
    
print("Enter array elements: ")
arr = [3, 1, 2, 5, 6]
print(arr)
tree = [0]*(4*(len(arr)))
build(arr, tree, 0, 0, len(arr) - 1) 

print("The segment tree is: ",tree) # only tree is built till here. We are yet to find range sum/max/min
# prefix sum is taking log(n) TC
print(f"Enter range between 0 to {len(arr)}")
l, r = map(int, input().split())
print("The sum of given range is: ", query(tree, 0, 0, len(arr) - 1, l, r)) # 2 3

print("Enter index and value to update: ")
i, val = map(int, input().split())
update(arr, tree, 0, 0, len(arr) - 1, i, val) # 2 5
print("Tree after updation is: ", tree)

