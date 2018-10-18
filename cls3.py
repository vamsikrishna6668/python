m =10
def matrimony(ma):
    print('This is a Website of Matrimony')
    return 2000
class bride:
    bridename ='ramesh'
    groomname ='sita'
    def usbride(self,i):
        self.s =i
        print('Iam a bride of a US')
    def ukbride(self):
        self.s =12000
        global m
        m+=58
        print(m)
        print(self.s)
        print('Iam a bride of a UK')
        print(self.bridename)
        print(self.groomname)
    @classmethod
    def groom(cls):
        cls.f=3456
        print(cls.bridename)
        print(cls.groomname)
        print(cls.f)
    @staticmethod
    def bridegroom(k,l):
        print(k)
        print(l)
        print(k+l)
        print('This is a matrimony website for bride and groom')
#calling block
matri=bride()
bride.bridegroom(100,68)
bride.groom()
matri.ukbride()
matri.usbride(80)
print(m)
