operator = input("enter the operator")

match operator:
    case "+":
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
        print(a+b)
    case "-":
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
        print(a-b)
    case "*":
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
        print(a*b)
    case "/":
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
        print(a/b)