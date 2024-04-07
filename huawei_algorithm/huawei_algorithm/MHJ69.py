matrix1_m = int(input())
matrix1_n = matrix2_m = int(input())
matrix2_n = int(input())

matrix1 = [list(map(int,input().split())) for _ in range(matrix1_m)]
matrix2 = [list(map(int,input().split())) for _ in range(matrix2_m)]

res_matrix = [[0]*matrix2_n for _ in range(matrix1_m)]

for i in range(matrix1_m):
    for j in range(matrix2_n):
        a = matrix1[i]
        b = [item[j] for item in matrix2]
        tmp = sum([item[0]*item[1] for item in zip(a,b)] )
        res_matrix[i][j] = tmp

for item in res_matrix:
    for atom in item:
        print(atom,end=" ")
    print()