def safe(board,row,col):
    for i in range(0,row):
        if board[i][col] == 1:
            return False
    r = row
    c = col # temporary variables are declared to use them for traversing and not to lose original value
    while r >= 0 and c < len(board):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1
    r = row
    c = col # temporary variables are declared to use them for traversing and not to lose original value
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    return True

def solve(board,row,n):
    if row == n:
        display(board)
        return
    for col in range(n):
        if safe(board,row,col):
            board[row][col] = 1
            solve(board,row+1,n)
            board[row][col] = 0

def display(board):
    for i in board:
        print(i)
    print()
        
n = int(input("Enter n: "))
board = [[0]*n for i in range(n)]
solve(board,0,n) # 0 is starting point/index ie., 0th row and n is ending


