class A:
    def __init__(self):
        self.comp_address=input("Enter a company Address:")
        self.comp_name=input("enter a company name:")
    def display(self):
        print(self.comp_address)
        print(self.comp_name)
#call
a1=A()
a1.display()
