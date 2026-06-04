matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:  
    for col in row:  
        print(col, end=" ")  
    print()
#for maximum element in the matrix
max = matrix[0][0]
for row in matrix:
    for col in row:
        if col > max:
            max = col
print("The maximum element in the matrix is:", max)
#for minimum element in the matrix
min = matrix[0][0]
for row in matrix:
    for col in row:
        if col < min:
            min = col
print("The minimum element in the matrix is:", min)    