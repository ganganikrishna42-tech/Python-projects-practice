num = int(input("Enter the size of the array:"))

def factorial_array(num):
    return [factorial(i) for i in range(num)]   
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
factorials = factorial_array(num)
print("The factorials of the array are:", factorials)    