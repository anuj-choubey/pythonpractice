matrix1 = ()
matrix2 = ()
matrix3 = ()

for i in range(3):
    temp1 = []

    for j in range(3):
        temp1.append(int(input("Enter Number : ")))

    matrix1 = list(matrix1)
    matrix1.append(temp1)
    temp1 = tuple(temp1)
    matrix1 = tuple(matrix1)
print(matrix1)
