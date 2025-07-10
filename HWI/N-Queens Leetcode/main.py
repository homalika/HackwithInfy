def safe(board,r,c):
    for i in range(0,r):
        if board[i][c]==1:
            return False
    row=r 
    col=c
    while row>=0 and col<len(board):
        if board[row][col]==1:
            return False 
        row-=1 
        col+=1
    row=r 
    col=c
    while row>=0 and col>=0:
        if board[row][col]==1:
            return False 
        row-=1 
        col-=1
    return True
def solve(board,row,n):
    if row==n:
        temp=[]
        for i in board:
            s=""
            for j in i:
                if j==1:
                    s=s+"Q"
                else:
                    s=s+"."
            temp.append(s)
        global l 
        l.append(temp)
        return
    for col in range(n):
        if safe(board,row,col):
            board[row][col]=1
            solve(board,row+1,n)
            board[row][col]=0
l=[]
n=int(input())
board=[[0]*n for i in range(n)]
solve(board,0,n)
print(l)
