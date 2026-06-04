matrix = [11,22,33],[44,55,66],[77,88,99]

sum = 0
for row in matrix:
    for col in row:
        sum += col  
print("The sum of the elements in the matrix is:", sum) 
