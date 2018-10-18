# w.a.p on class example by static method and static variables  and take a local variable also print without a reference variable?
class Employee:
     comp_name="IBM"
     comp_add="Hyd"
     @staticmethod
     def assign(i,j):
         k=100
         print(k)
         print(i+j)
         print("Iam a assign method")
#call
print(Employee())
print(Employee().comp_name)
print(Employee().comp_add)
Employee.assign(10,20)