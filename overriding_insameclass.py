class Student:
    def __init__(self):
        self.idno=input("Enter a Idno:")
        print("Iam a Constructor")
    def assign(self):
        self.name=input("Enter a Student Name:")
        self.std_course=input("Enter a student course:")
        print("Iam assign Method 1")
    def assign(self):
        self.name = input("Enter a Student Name:")
        self.std_course = input("Enter a student course:")
        print("Iam assign Method 2")
#call
s=Student()
s.assign()