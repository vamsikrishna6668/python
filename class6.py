class Employee:
    comp_wiki=input("Enter a company wiki:")
    comp_loca=input("Enter a company Location:")
    def assign(self,idno,name):
        self.idno=idno
        self.name=name
        print("Iam a Assign Method")
    def display(self,salary,address):
        print(self.idno)
        print(self.name)
        self.salary=salary
        self.address=address
        print(self.salary)
        print(self.address)
        print("Iam a display Method")
#call
x=int(input("Enter a idno:"))
y=input("Enter a Name:")
e1=Employee()
e1.assign(x,y)
e1.display(1850000,'Hyd')
print("============================")
e1.display(7800000,'Bng')
