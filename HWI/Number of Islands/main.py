def fun(i,j,g):
    if i < 0 or i >= len(g) or j < 0 or j >= len(g[0]):
        return
    if g[i][j] == 0:
        return
    g[i][j] = 0
    
    fun(i-1,j,g)
    fun(i+1,j,g)
    fun(i,j+1,g)
    fun(i,j-1,g)
    
n = [[1,0,0,1],
     [0,1,1,0],
     [0,0,0,1],
     [1,0,0,1]]
c = 0
for i in range(len(n)):
    for j in range(len(n[0])):
        if n[i][j] == 1:
            c += 1 
            fun(i, j, n)
print(c)            
            
            