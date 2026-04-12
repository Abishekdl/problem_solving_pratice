A = [[1, 2, 3],
     [2, 5, 6],
     [3, 6, 9]]

for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] !=A[j][i]:
            print("It is not symmetric")
        else:
            print("It is symmetric")
    
