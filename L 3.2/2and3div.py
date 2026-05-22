for i in range(1, 51):
    if i  % 2 == 0 and i % 3 == 0:
        print("divisible by both 2 and 3:", i)
    elif i % 2 == 0:
        print("divisible by 2:", i)
    elif i % 3 == 0:
        print("divisible by 3:", i)        