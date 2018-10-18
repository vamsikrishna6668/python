class item:
    def __init__(self,idno,name,price):
        self.idno=idno
        self.name=name
        self.price=price
    def __eq__(self,other):
        if self.name.lower() ==other.name.lower() and self.price==other.price:
            return True   # lower is a lowercase in the pgm.
        else:
            return False
#calling block
i1=item(66,'ISMAil',80000)
i2=item(68,'ismail',80000)
print(i1==i2)

