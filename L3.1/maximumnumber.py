a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a>b:
    if a>c:
        print("first number is the greatest")
    else:
        print("third number is the greatest")
else:
    if b>c:
        print("second number is the greatest")
    else:
        print("third number is the greatest")