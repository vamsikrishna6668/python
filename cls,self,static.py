a =10
class ImageHospitals:
    hospitallocat ='Hyd'
    hospitalbranc = 'Ameerpet'
    @staticmethod
    def fever(viral,dengu):
        print('The viral fever =',viral)
        print('The dengu fever =',dengu)
        print('This is a Fever department')
    @classmethod
    def eyes(cls):
        cls.eyebucks =120335
        print(cls.hospitallocat)
        print(cls.hospitalbranc)
        print('This is the eye operation bucks:',cls.eyebucks)
        print('This is a Eye Department')
    def bodyscan(self,n):
        self.i =n
    def scan1(self):
        print('This is a  scan1 department')
        self.i =100
        print(self.i)
        global a
        a += 58
        print('This is a Global variable value:', a)
#calling block
hospit =ImageHospitals()
ImageHospitals.fever(102,104)
ImageHospitals.eyes()
hospit.scan1()
