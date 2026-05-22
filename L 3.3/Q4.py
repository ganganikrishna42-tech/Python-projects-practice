strt_no= int(input("Enter the starting number: "))
end_no= int(input("Enter the ending number: "))
for i in range(strt_no, end_no+1):
    for j in range(1,11):
        print(i, "x", j, "=", i*j)
        