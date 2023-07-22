a_r = int(input("Enter the no. of rows of matrix A: "))
a_c = int(input("Enter the no. of cols of matrix A: "))
b_r = int(input("Enter the no. of rows of matrix B: "))
b_c = int(input("Enter the no. of cols of matrix B: "))
          
mat_a = []
mat_b = []
mat_c = []

for x in range(0, a_r):
    row = []
    mat_c.append(row)
    for y in range(0, b_c):
        row.append(0)

if a_c == b_r:
    print("Matrix A")
    for x in range(0, a_r):
        row = []
        mat_a.append(row)
        for y in  range(0, a_c):
            row.append(int(input(f"Enter Element {x}{y}: ")))

    print("Matrix B")
    for x in range(0, b_r):
        row = []
        mat_b.append(row)
        for y in  range(0, b_c):
            row.append(int(input(f"Enter Element {x}{y}: ")))

    print("\nMatrix A")
    print(mat_a)
    print("\nMatrix B")
    print(mat_b)

    for i in range(0,a_r):
        for j in range(0,b_c):
            for k in range(0,a_c):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j]

    print("\nMatrix C")
    print(mat_c)
        
else:
    print("Matrix Multiplication is not supported for the given dimensions!!")