# Write a program to multiply two matrices as nested lists.

rows_A = int(input("Enter number of rows in Matrix A: "))
cols_A = int(input("Enter number of columns in Matrix A: "))
rows_B = int(input("Enter number of rows in Matrix B: "))
cols_B = int(input("Enter number of columns in Matrix B: "))

if cols_A != rows_B:
    print("Matrix multiplication not possible. Columns of A must equal rows of B.")
else:
    print("Enter elements of Matrix A row-wise:")
    A = []
    for i in range(rows_A):
        row = [int(x) for x in input(f"Row {i+1}: ").split()]
        A.append(row)

    print("Enter elements of Matrix B row-wise:")
    B = []
    for i in range(rows_B):
        row = [int(x) for x in input(f"Row {i+1}: ").split()]
        B.append(row)

    result = []
    for i in range(rows_A):
        result.append([0] * cols_B)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)