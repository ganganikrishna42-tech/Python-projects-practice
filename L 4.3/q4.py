a = [11, 22, 33, 44, 55,66,77,88,99]
print("the given list is: ",a)
b =int(input("Enter the number you want to delete: "))
if b in a:
    a.remove(b)
    print("the list after deleting the number is: ",a)
else:
    print("the number is not in the list")
print("the list after deleting the number is: ",a)    