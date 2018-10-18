class Company:
    comp_wikipedia=input("Enter a Wikipedia website name:")
    comp_Branches=input("Enter a Company Branches Names:")
    def __init__(self):
        self.comp_USA=input("Enter a Company of USA Address:")
        self.comp_TurnOver=int(input("Enter a Turn Over Budget of a company:"))
        print("The Company address of USA:",self.comp_USA)
        print("The Company TurnOver of Every Year:",self.comp_TurnOver)
        print("Iam a Constructor")
        print("The Company Wikipedia Page:",Company.comp_wikipedia)
        print("The Company Branches across the World:",Company.comp_Branches)
    def assign(self):
        while True:
            try:
                self.comp_blockname=input("Enter Company Block Name:")
                self.comp_Noof_Floors=int(input("Enter Company No of floors:"))
                print(self.comp_blockname)
                print(self.comp_blockname)
                print("Iam Assign Method")
                ans=input("Enter continue to press Y/y:")
                if ans=='y' or ans=='Y':
                    continue
                else:
                    break
            except:
                print("Invalid Input")
    def show(self):
        while True:
            try:
                 comp_Totalnoof_Developers=int(input("Enter a total no of Developers in a company:"))
                 comp_Totalnoof_Testers=int(input("Enter a total no of testers in a company:"))
                 print("Iam a Show Method")
                 ans = input("Enter continue to press Y/y:")
                 if ans == 'y' or ans == 'Y':
                     continue
                 else:
                     break
            except:
                print("Invalid Input")
    def display(self,comp_Noofemployees,comp_startofyear):
        print(comp_Noofemployees)
        print(comp_startofyear)
        print("Iam  Display Method")
#call
c1=Company()
c1.assign()
c1.show()
c1.display(400,2018)

