class Employee:
    emp_desgination=input("Enter a Employee Desgination:")
    emp_work_loaction=input("Enter a Employee Work Location:")
    def fun1(self):
        print("Iam a function1")
    def assign(self,idno,name,sal):
        print("The idno of the Employee:",idno)
        print("The Name of the Employee:",name)
        print("The Salary of the Employee:",sal)
    def show(self,emp_add,emp_wiki):
        self.emp_add=emp_add
        self.emp_wiki=emp_wiki
        print(self.emp_wiki)
        print(self.emp_add)
    def display(self,age,cno):
        self.age=age
        self.cno=cno
        print("Iam a Display")
#call
e1=Employee()
e1.fun1()
e1.assign(101,"Ismail",96000000)
a=input("Enter a Employee address:")
b=input("Enter a Employee Wiki:")
e1.show(a,b)
e1.display(25,8500580594)