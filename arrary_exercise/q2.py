arr = [int(input("Enter a number:")) for i in range(int(input("Enter the size of the array:")))]
def square_array(arr):
    return [x**2 for x in arr]  
print("The squared array is:", square_array(arr))