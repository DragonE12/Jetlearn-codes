"""list_2d = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]
print(list_2d[0][2])
for num in list_2d:
    for num1 in num:
        print(num1, end = " ")
    print()"""


"""list_2d = []
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    row = []
    for a in range(columns):
        value = int(input("Enter the value: "))
        row.append(value)
    list_2d.append(row)
for row in list_2d:
    print(row)

matrix = []
num = int(input("Enter the dimensions of the matrix: "))
for i in range(num):
    bob = []
    for a in range(num):
        x = int(input("Enter the value: "))
        bob.append(x)
    matrix.append(bob)
for i in range(num):
    print(matrix[i][i])"""



"""matrix_a = [[1,2], 
            [3,4]]
matrix_b = [[2,1000],
            [4,8]]
addition_result = [[0,0],
                   [0,0]]
subtraction_result = [[0,0], 
                      [0,0]]
for i in range(0,2):
    for j in range(0,2):
        addition_result[i][j] = matrix_a[i][j] + matrix_b[i][j]
        subtraction_result[i][j] = matrix_a[i][j] - matrix_b[i][j]
for i in range(2):
    for j in range(2):
        print(addition_result[i][j], end = " ")
    print()
for i in range(2):
    for j in range(2):
        print(subtraction_result[i][j], end = " ")
    print()"""
        
matrix_a = [[5,9], 
            [20,69]]
matrix_b = [[3,7],
            [27,58]]
multiplication_result = [[0,0],
                        [0,0]]
for i in range(0,2):
    for j in range(0,2):
        multiplication_result[i][j] = matrix_a[i][j] * matrix_b[i][j]
for i in range(2):
    for j in range(2):
        print(multiplication_result[i][j], end = " ")
    print()
