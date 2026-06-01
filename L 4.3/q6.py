a = [11,22,33,44,55,66,77,88,99]
b = int(input("Enter the number to find its index: "))
if b in a:
    print("The index of", b, "is:", a.index(b))
else:
    print("The number is not in the list")