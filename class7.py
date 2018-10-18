a=1900
print(a)
def fun1(b,c):
    z=b
    y=c
    print(z+y)
    print("Iam a  Fucntion 1")
class Student:
    std_idno=int(input("Enter a Student Idno:"))
    std_name=input("Enter  a Student Name:")
    def fun2(self,schl_name,schl_address):
        self.sch1_name=schl_name
        self.sch1_address=schl_address
        global a
        a+=100
        print(a)
        print("Iam a Function 2")
    def Display(self):
        print("Iam a  Display")
        global a
        a*=20
        print(a)
        print(self.sch1_name)
        print(self.sch1_address)
    @staticmethod
    def static(i,j):
        s=i
        t=j
        print(s+t)
        print("Iam a Static method")
    @classmethod
    def clasmethod(cls):
        print(cls.std_idno)
        print(cls.std_name)
        print("Iam a Class Method")
#call
print(a)
f=fun1(20,10)
s1=Student()
s1.fun2("Nagarjuna public school","Mangalagiri")
s1.Display()
s1.static(60,30)
s1.clasmethod()
