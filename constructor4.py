class Railway:
    rail_office_Locat=input("Enter a railway station office Location:")
    rail_No_Of_Counters=int(input("Enter No of counters in the railway station:"))
    def __init__(self):
        self.rail_No_Of_Employees=int(input("Enter no of employees in the Railway Department:"))
        self.rail_No_Of_Trains=int(input("Enter a number of trains:"))
        print(self.rail_No_Of_Employees)
        print(self.rail_No_Of_Trains)
    def assign(self,idno,name):
        self.idno=idno
        self.name=name
        print("Iam assign Method")
    def show(self):
        while True:
            try:
                self.no_of_platform=int(input("Enter a no of platforms:"))
                self.no_of_trainsNames=input("Enter a no of train names:")
                print(self.no_of_platform)
                print(self.no_of_trainsNames)
                print("Iam Show Method")
                ans=input("Enter a continute press Y/y:")
                if ans=='y' or ans=='Y':
                    continue
                else:
                    break
            except:
                print("Invalid Input")
        print("Iam show Method")
    def display(self,No_Railwaytraindrivers,No_Railwaytrain_Tc):
         print("Enter total no of Railway trains drivers:",No_Railwaytraindrivers)
         print("Enter total no of Railway trains tc's:",No_Railwaytrain_Tc)
         print("Iam Display Method")
#calling
r1=Railway()
print(r1.rail_office_Locat)
print(r1.rail_No_Of_Counters)
a=int(input("enter a idno of Railway person:"))
b=input("enter a name of the Employee:")
r1.assign(a,b)
r1.show()
r1.display(50,100)



