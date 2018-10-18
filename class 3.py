class Employee:
    def assign(self):
        self.empidno=int(input("Enter a Employee idno:"))
        self.empname=input("Enter a Employee name:")
        self.empsalary=float(input("Enter a Employee Salary:"))
        print("Iam a Assign Method")
    def display(self):
        print("The Employee idno:",self.empidno)
        print("The Employee empname:",self.empname)
        print("The Employee salary",self.empsalary)
        print("Iam a display Method")
#call
e1=Employee()
e1.assign()
e1.display()