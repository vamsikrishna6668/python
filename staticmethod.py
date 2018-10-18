c =78
class pscmr():
    employeename ='chanti'
    employeefriends ='sai','raj','rakes','bala','sati','ism','anji','vam'
    def sai(self,b):           # self is a Instance variable
        self.b =1000
        global c
        c+=10
        print(c)
        print(self.employeename)
        print(self.employeefriends)
        print('This is a sai Teja')
    def raj(self):
        self.b+=68
        print(self.b)
        print('This is a rajesh')
#calling block
a =pscmr()
a.sai(10)
a.raj()
print(c)
