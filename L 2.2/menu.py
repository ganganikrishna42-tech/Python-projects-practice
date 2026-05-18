food = input("press 1 to order pizza, 2 to order burger, 3 to order pasta: ")

match food:
    case "1":
        print("you chose pizza press 5 to get cheese pizza, 6 to get thin crust pizza: ")
        match 1:
            case "5":
                print("cheese pizza")
            case "6":
                print("thin curst pizza")    
    case "2":
        print("you chose burger press 7 to get cheese burger, 8 to get chicken burger: ")
        match 2:
            case "7":
                print("cheese burger")
            case "8":
                print("chicken burger")
    case "3":
        print("you chose pasta press 9 to get white sauce pasta, 10 to get red sauce pasta: ")
        match 3:
            case "9":
                print("white sauce pasta")
            case "10":
                print("red sauce pasta")

  