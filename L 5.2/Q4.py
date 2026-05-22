a = [1,2,3,4,5,6,7,8,9,10]

b= [i**2 for i in a ] 
print(b)


c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

d=[i for i in c if i%2==0]
print(d)


wrd=["hello","WORLD","PyThOn"]
e=[i.lower() for i in wrd]
print(e)