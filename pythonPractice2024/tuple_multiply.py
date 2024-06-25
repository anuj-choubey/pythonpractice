mat1 = (
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3)
)
mat2 = (
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3)
)
mat3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(mat1)):

    for j in range(len(mat2[0])):
        multiply_of_matrix_result = []
        for k in range(len(mat2)):
            product = (mat1[i][k] * mat2[k][j])
            multiply_of_matrix_result.append((mat1[i][k], mat2[k][j], product))
            mat3[i][j] += product

mat3 = tuple(mat3)
print(mat3, end=" ")
