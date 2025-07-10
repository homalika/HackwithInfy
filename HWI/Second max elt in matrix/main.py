row = int(input("Rows: "))
col = int(input("Columns: "))
matrix = []
print("Enter matrix: ")
for i in range(row):
    rows = []
    for j in range(col):
        rows.append(int(input()))
    matrix.append(rows)
print("Matrix is: ")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end =" ")
    print()
maxi = smax = 0    # or maxi = matrix[0][0]
for i in range(row):
    for j in range(col):
        if matrix[i][j] > maxi:
            smax = maxi
            maxi = matrix[i][j]
        elif maxi > matrix[i][j] > smax:
            smax = matrix[i][j]
print("Largest element in matrix is:", maxi)
print("Second largest element in matrix is:", smax)