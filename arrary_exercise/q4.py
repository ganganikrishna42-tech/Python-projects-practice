arr1 = [int(input("Enter a number:")) for i in range(int(input("Enter the size of the array:")))]
arr2 = [int(input("Enter a number:")) for i in range(int(input("Enter the size of the array:")))]

def merge_arrays(arr1, arr2):
    merged_array = arr1 + arr2
    return merged_array 
merged_array = merge_arrays(arr1, arr2)
print("The merged array is:", merged_array)

arr3 = [int(input("Enter a number:")) for i in range(int(input("Enter the size of the array:")))]
def merge_arrays(arr1, arr2, arr3):
    merged_array = arr1 + arr2 + arr3
    return merged_array
merged_array = merge_arrays(arr1, arr2, arr3)
print("The merged array is:", merged_array)