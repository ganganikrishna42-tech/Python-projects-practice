a = [11, 22, 33, 44, 55]
b = int(input("Enter the number you want to insert: "))
c = int(input("Enter the index where you want to insert the number: "))
a.insert(c, b)  # Insert 'b' at index 'c'
print(a)