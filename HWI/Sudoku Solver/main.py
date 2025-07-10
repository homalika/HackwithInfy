def issafe(mat, r, c, n):
    # row
    for i in range(len(mat)):
        if mat[i][c] == n:
            return False
    # col 
    for i in range(len(mat[0])):
        if mat[r][i] == n:
            return False
    rstart = 3*(r//3)
    cstart = 3*(c//3)
    for i in range(rstart, rstart+3):
        for j in range(cstart, cstart+3):
            if mat[i][j] == n:
                return False
    return True

def solve(mat):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                for n in range(1, 10):
                    if issafe(mat, r, c, n):
                        mat[r][c] = n 
                        if solve(mat):
                            return True
                        mat[r][c] = 0 
                return False
    return True

def display(mat):
    for i in mat:
        print(i)

mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
      ]
if solve(mat):
    display(mat)
else:
    print("Not Valid.")
    