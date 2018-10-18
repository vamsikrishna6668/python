class schl_student:
    std_idno=int(input("Enter  a student Idno:"))
    std_name=input("Enter a Student Name:")
    def __init__(self):
        self.std_class=input("Enter a student which class he/she belong to:")
        self.std_lang=input("Enter a student Mother Tongue Language:")
        print("Iam  a Constructor")
    def assign(self):
        while True:
            try:
                self.std_age=int(input("Enter a Student Age:"))
                self.std_marks=int(input("Enter a student marks:"))
                print(self.std_age)
                print(self.std_marks)
                print(schl_student.std_idno)
                print(schl_student.std_name)
                ans=input("Enter a continue press Y/y:")
                if ans=='y' or ans=='Y':
                    continue
                else:
                    break
            except:
                print("Invalid Input")

    def display(self):
        print("Iam a Display Method")

#call
s1=schl_student()
s1.assign()
s1.display()

