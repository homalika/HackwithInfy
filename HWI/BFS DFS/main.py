# Breadth First Search
g = {1:[2,3], 2:[4,5], 3:[6,7]}
i = 1 # from which index we start
q = [i]
while q:
    c = q.pop(0) # popping 1st elt from queue
    print(c)
    if c in g:
        for neigh in g[c]: # g[i] is dict of i 
            q.append(neigh)
print()
# Depth First Search
g = {1:[2,3], 2:[4,5], 3:[6,7]}
i = 1 # from which index we start
q = [i]
while q:
    c = q.pop() # popping last elt in stack
    print(c)
    if c in g:
        for neigh in g[c]: # g[i] is dict of i 
            q.append(neigh)