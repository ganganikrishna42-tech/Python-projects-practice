class person:
    name = input("Enter the name of the person:")
    age = int(input("Enter the age of the person:"))
   
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = person()
p1.display()        