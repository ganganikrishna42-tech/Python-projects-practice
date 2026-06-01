a = [11,22,33,44,55,66,77,88,99]
b = int(input("Enter the number you want to update : "))

if b in a:
    c = int(input("Enter the index where you want to update the number: "))
    a[c] = b
    print("the list after updating the number is: ",a)