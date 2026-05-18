food = input("press 1 to order pizza, 2 to order burger, 3 to order pasta: ")

match food:
    case "1":
        print("you chose pizza press 5 to get cheese pizza, 6 to get thin crust pizza: ")
        pizza = input("press 5 or 6: ")
        match pizza:
            case "5":
                print("order of cheese pizza is placed")
            case "6":
                print("order of thin crust pizza is placed")
    case "2":
        print("you chose burger press 7 to get cheese burger, 8 to get chicken burger: ")
        burger = input("press 7 or 8: ")
        match burger:
            case "7":
                print("order of cheese burger is placed")
            case "8":
                print("order of chicken burger is placed")
    case "3":
        print("you chose pasta press 9 to get white sauce pasta, 10 to get red sauce pasta: ")
        pasta = input("press 9 or 10: ")
        match pasta:
            case "9":
                print("order of white sauce pasta is placed")
            case "10":
                print("order of red sauce pasta is placed")

  