age = int(input("enter your age here"))
if age>=0 and age < 13:
    print("the person is a child")
elif age>=13 and age <=19: 
    print("the person is teenager")
elif age>=20 and age <=59:
    print("the person is an adult")
elif age>=60:
    print("the person is senoir")
else:
    print("enter an appropriate age ")
