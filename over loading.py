class institute:
    def __init__(self,training,price):
        self.sathyatraining =training
        self.sathyprice=price

    def __eq__(self, other):
        if self.sathyatraining.lower()==other.sathyatraining.lower() and self.sathyprice==other.sathyprice:
            return 'sathya insitute is good'
        else:
            return 'sathya insitute is avg'
#calling block
a =institute('SathyA',20)
b=institute('sathya',20)
print(a==b)