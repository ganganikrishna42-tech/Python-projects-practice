tup = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15)]
for row in tup:
    for col in row:
        print(col, end=" ")
    print() 
sorted_tup = sorted(tup, key=lambda x: x[0])
print("The sorted tuple is:", sorted_tup)    