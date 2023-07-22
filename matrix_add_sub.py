r = int(input("Enter the Row Count: "))
c = int(input("Enter the Column Count: "))

mat_a = []
mat_b = []
mat_sum = []
mat_diff = []

for x in range(0, r):
    row1 = []
    row2 = []
    mat_sum.append(row1)
    mat_diff.append(row2)
    for y in range(0, c):
        row1.append(0)
        row2.append(0)

print("Matrix A")
for x in range(0, r):
    row = []
    mat_a.append(row)
    for y in  range(0, c):
        row.append(int(input(f"Enter Element {x}{y}: ")))

print("Matrix B")
for x in range(0, r):
    row = []
    mat_b.append(row)
    for y in  range(0, c):
        row.append(int(input(f"Enter Element {x}{y}: ")))

print("\nMatrix A")
print(mat_a)
print("\nMatrix B")
print(mat_b)

for x in range(0,r):
    for y in range(0,c):
        mat_sum[x][y] = mat_a[x][y] + mat_b[x][y]
        mat_diff[x][y] = mat_a[x][y] - mat_b[x][y]

print("\nThe sum of the two matrices is:")
print(mat_sum)
print("\nThe difference of the two matrices is:")
print(mat_diff)


