class Employee:
    emp_name=input("Enter a Name of a Employeee:")
    emp_Desgin=input("Enter a Designation of a Employee:")
    def assign(self):
        self.idno=int(input("Enter a idno:"))
        self.salary=float(input("Enter a salary:"))
    def display(self):
        print("The Name of the Employee:",Employee.emp_name)
        print("The Designation  of the Employee:",Employee.emp_Desgin)
        print("The Idno of the Employee:",self.idno)
        print("The salary of the Employee:",self.salary)
#calll
e1=Employee()
e1.assign()
e1.display()
print(Employee().emp_Desgin)
print(Employee().emp_name)