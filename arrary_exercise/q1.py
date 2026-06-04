a = int(input("Enter the size of the array:"))
num = [input("Enter a number:") for i in range(a)]
odd_num = [x for x in num if int(x) % 2 != 0]
print("\nThe odd numbers in the array are:\n", odd_num)
even_num = [x for x in num if int(x) % 2 == 0]
print("\nThe even numbers in the array are:\n", even_num)