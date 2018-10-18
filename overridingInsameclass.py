class Student(object):
    def __init__(self):
        print("Iam a constructor")
    def assign(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
        print("Iam a Method of assign 1")
    def assign(self,a,b):
        self.a=a
        self.b=b
        print(self.a*self.b)

#call
s=Student()
s.assign(20,10)