# Example pgm to assign different values for Instance variables  for every Object?
class Employee:
    comp_name=input("Enter a Company name:")
    comp_wiki=input("Enter a wiki of the Company:")
    def assign(self):
        self.salary=float(input("Enter a Employee salary:"))
        self.comp_loca=input("Enter a Employee company Location:")
        self.comp_address=input("Enter a company address:")
        print("Iam a assign method:")
    def display(self):
        print("Iam a display")
        print("The employeee salary:",self.salary)
        print("The Employeee company name:",self.comp_name)
        print("The Employeee company address:",self.comp_address)
        print(Employee.comp_name)
        print(Employee.comp_wiki)
#calll
e1=Employee()
e1.assign()
e1.display()
print("===============================")
print(Employee().comp_name)
print(Employee().comp_wiki)
