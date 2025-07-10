def solve(board,word,n,i,j):
    if n == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[n]:
        return False
    t = board[i][j]
    board[i][j] = '*'
    if solve(board,word,n+1,i+1,j) or solve(board,word,n+1,i-1,j) or solve(board,word,n+1,i,j+1) or solve(board,word,n+1,i,j-1):
        return True
    board[i][j] = t

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == word[0]:
            if solve(board,word,0,i,j):
                print(True)
                break
else:
    print(False)