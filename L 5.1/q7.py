class student:
    name = input("Enter the name of the student:")
    subjects = input("Enter the subjects of the student:").split(',')
    marks = int(input("Enter the marks of the student:"))


    def display(self):
        print("Name:", self.name)
        print("Subjects:", self.subjects)
        print("Marks:", self.marks)
s1 = student()
s1.display()    
