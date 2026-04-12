A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

value = 0
j = 0
for i in range(len(A)):
    # if i == j:
    #     value += A[i][j]
    #     j +=1
    value += A[i][i]

print(value)
