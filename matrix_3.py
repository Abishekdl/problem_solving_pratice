A = [[1, 2, 3],
     [4, 5, 6]]


row_a = len(A)
col_a= len(A[0])

result = [[0] * row_a for i in range(col_a)]

for i in range(row_a):
    for j in range(col_a):
        # for k in range(row_a):
        result[j][i] = A[i][j] 

print(result)
