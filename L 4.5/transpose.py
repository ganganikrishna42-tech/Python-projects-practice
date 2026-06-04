row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

arr = []
print("Enter the elements of the array:")
for i in range(row):
    arr.append(list(map(int, input().split()))) 
print("The original array is:")

for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print()
print("The transposed array is:")
for i in range(col):
    for j in range(row):
        print(arr[j][i], end=" ")
    print()