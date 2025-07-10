row = int(input("Rows: "))
col = int(input("Columns: "))
matrix = []
print("Enter matrix: ")
for i in range(row):
    rows = []
    for j in range(col):
        rows.append(int(input()))
    matrix.append(rows)             # also try appending col wise
print("Matrix is: ")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end =" ")
    print()
maxi = matrix[0][0]
for i in range(row):
    for j in range(col):
        if matrix[i][j] > maxi:
            maxi = matrix[i][j]
print("Maximum element in matrix is:", maxi)