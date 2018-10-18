q=500
class deloitte:
    comp_name ='delo'
    comp_cno =880183
    def tsconsultancy(self,i,d):
        global q
        q+=68
        self.c=d
        self.i =1200
        print('This is a Global variable=',q)
        print('It is a Tsconsultancy')
    def show(self):
        print('Iam show')
        self.c=9796
        self.i+= 34
        print(self.c)
        print(self.i)
        print(self.comp_name)
        print(self.comp_cno)
        print('This is a end of the Instance Method')
    @staticmethod
    def display(a,l):
        global q
        q =66
        print(q)
        print('This is a Global variable in static method')
        print(a)
        print(l)
        print(a*l)
        print('Iam display')
        print(deloitte.comp_name)
        print(deloitte.comp_cno)
        print('This is a end of a Static Method')
    @classmethod
    def meth(cls):
        cls.a =100
        global q
        q =97
        print(q)
        print('This is a Global variable in class method')
        print('Iam a class method')
        print(cls.comp_name)
        print(cls.comp_cno)
        print(cls.a)
        print('This is a end of a Class Method')
#calling block
tobj =deloitte()
deloitte.meth()
deloitte.display(90,81)
tobj.tsconsultancy(10,760)
tobj.show()


