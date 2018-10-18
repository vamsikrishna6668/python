class schl_student:
    std_idno=int(input("Enter  a student Idno:"))
    std_name=input("Enter a Student Name:")
    def __init__(self):
        self.std_class=int(input("Enter a student which class he/she belong to:"))
        self.std_lang=input("Enter a student Mother Tongue Language:")
        print("Iam  a Constructor")
    def assign(self):
        while True:
            self.std_add=input("Enter a Student Address:")
            self.std_locat=input("Enter a student Location:")
            ans=input("Enter a continute press Y/y:")
            if ans=='y' or ans=='Y':
                continue
            else:
                break
    def display(self):
        print(self.std_locat)
        print(self.std_add)
        print(schl_student.std_idno)
        print(schl_student.std_name)
#call
s1=schl_student()
s1.assign()
s1.display()

