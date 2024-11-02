def build_matrix(column, row):
    matrix = []
    for i in range(column):
        a = []
        for j in range(row):
            a.append(int(input(f"Enter data for matrix: ")))
        matrix.append(a)
    return matrix

def print_matrix(matrix, row, column):
    for i in range(column):
        for j in range(row):
            print(matrix[i][j], end = " ")
        print()

def product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        a = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            a.append(sum)
        result.append(a)
    return result

def print_result_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

matrix1 = []
matrix2 = []
column1, row1 = map(int, input("Enter a size for 1 matrix: ").split(", "))
column2, row2 = map(int, input("Enter a size for 2 matrix: ").split(", "))
if row1 == column2:
    matrix1 = build_matrix(column1, row1)
    matrix2 = build_matrix(column2, row2)
    print("Your 1 matrix is: ")
    print_matrix(matrix1, row1, column1)
    print("Your 2 matrix is: ")
    print_matrix(matrix2, row2, column2)
else:
    print("Try again")
result_matrix = product(matrix1, matrix2)
print("The product of the matrices is: ")
print_result_matrix(result_matrix)