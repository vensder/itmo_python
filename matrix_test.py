# test transpons matrix

dim = 10
matrix = [[i for i in range(dim)] for i in range(dim)]
matrix_t = [[0 for i in range(dim)] for i in range(dim)]

for i in range(dim):
    for j in range(dim):
        matrix_t[i][j] = matrix[j][i]

for row in matrix:
    print(row)

for row in matrix_t:
    print(row)

