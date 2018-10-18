s =64    # global variable
def sat(q):                     # This is a function.
    print('ismail basha')
class sathya:
    institute ='sathya Technologies'    # static variables
    branchname ='Ameerpet'              # static variables
    def naveen(self,a):      #self is a instance variable and a is a local variable
        self.x =a
        print('Naveen sir  is a professor')
    def python(self,py):      # 2nd Instance method.
        self.x =6866
        self.py =4512123456
        print(self.x)
        print(self.py)
        print('This is a python')
    @classmethod
    def morningbatch(cls):
        cls.n =81
        global s
        s+=4
        print('This is a Morning Batch of Python')
        print(cls.institute)
        print(cls.branchname)
        print(cls.n)
        print(s)
    @staticmethod
    def sevenclockbatch(g,p):
        print(g)
        print(p)
        print(g+p)
        print(sathya.institute)
        print(sathya.branchname)
        print('This is a seven clock batch')
#calling block
web = sathya()
sathya.morningbatch()        # class method can be called with a class name or with a object name.
sathya.sevenclockbatch(66,68)  # class method can be called with a class name or with a object name.
web.python(48)                # Instance method can be called with only variable name only.
web.naveen(10)               # Instance method can be called with only variable name only.
w=sat(10)
print(w)
web.morningbatch()       # class method can be called with a class name or with a object name.
