year = [int(input("Enter a year:")) for i in range(int(input("Enter the number of years:")))]
leap_years = [x for x in year if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)]
print("\nThe leap years in the array are:\n", leap_years)