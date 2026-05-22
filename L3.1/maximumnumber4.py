a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
d = int(input("Enter a fourth number: "))

if a > b:
    if  a > c:
        if a > d:
            print("first number is the greatest")
        else:
            print("fourth number is the greatest")
else:    
    if b > c:
        if b > d:
            print("second number is the greatest")
        else:
            print("fourth number is the greatest")      
    else:       
        if c > d:
            print("third number is the greatest")   


