class Employee:
    comp_name='IBM'
    comp_contact=8500580594
    def details(self,pf,da,hra,salary,total):
        self.pf=pf
        self.da=da
        self.hra=hra
        self.salary=salary
        self.total =total
        self.total1=self.salary*self.pf
        self.total2=self.salary*self.da
        self.total3=self.salary* self.hra
    def display(self):
        print("This is a employee's pf:=",self.pf)
        print("This is a employee's daily wages:",self.da)
        print("This is a Employee's hourly rates of money:=",self.hra)
        print("This is a Employee's salary:=",self.salary)
        print("This is a Employee's total:=",self.total)
        print("These are employee's details of a salary and pf:=",self.total1)
        print("These are employee's details of a salary and pf:=", self.total2)
        print("These are employee's details of a salary and pf:=", self.total3)
#calling block
emp=Employee()
print(Employee.comp_name)
print(Employee.comp_contact)
emp.details(12,20,23,45,64)
emp.display()
