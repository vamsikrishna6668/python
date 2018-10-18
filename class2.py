# w.a.p on class example by static method and static variables  and take a local variable also print without a reference variable?

class student:
    std_idno=101
    std_name="ismail"
    @staticmethod
    def assign(b,c):
        a=1000
        print("The Local variable value:",a)
        print("The static variable name:",student.std_name)
        print("The static variable idno: ",student.std_idno)
        print("Iam a static method")
        print(b*c)
#call
student.assign(50,60)
print(student().std_idno)
print(student().std_name)
