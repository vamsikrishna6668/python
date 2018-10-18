class Faculty:
    def __init__(self):
        self.Facu_idno=int(input("Enter a faculty Idno number:"))
        print("Iam a constructor of Faculty")
    def assign(self,name):
        self.Facu_name=name
        print(self.Facu_name)
        print("Iam a Method of Assign 1")
class Student(Faculty):
    def __init__(self):
        self.Std_idno=int(input("Enter a  Student Id  number:"))
        print("Iam a construcotr of student")
        super().__init__()
    def assign(self,name):
        self.Std_name=name
        print(self.Std_name)
        print("Iam a  method of a Assign 2")
        super().assign(name)
#call
s=Student()
a=input("Enter a Name:")
s.assign(a)

