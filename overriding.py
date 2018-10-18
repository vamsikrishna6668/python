class Student:
    def __init__(self):
        self.idno=int(input("enter a number:"))
        print("Iam a Constructor of Idno")
    def __init__(self):
        self.name=input("Enter a name:")
        print("Iam a Constructor of name")
    def __init__(self):
        self.qualification=input("Enter a qualification:")
        print("Iam a Constructor of salary")
    def assign(self):
        while True:
            self.course_fee=int(input("Enter a student course Fee:"))
            self.std_course=input("Enter a student course names:")
            ans=input("Enter continue to press y/Y:")
            if ans=='Y' or ans=='y':
                continue
            else:
                break
        print("Iam a Method of assign")
#call
s=Student()
s.assign()