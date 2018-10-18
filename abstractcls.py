from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class card(payment):
    def pay(self,amount):
        self.amount=amount
        print(self.amount,'paid with a card')
#calling block
c =card()
c.pay(50000)