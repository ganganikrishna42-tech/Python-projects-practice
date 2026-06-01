a = [1,2,3,4,5,6]
b = [7,8,9,10,11,12]
print("the original list is: ",a)
print("the second list is: ",b)
for i in b:
    a.append(i)
print("the merged list is: ",a)