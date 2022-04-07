from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Suit(Clothes):
    def __init__(self,height):
        self.height = height

    @property
    def consumption(self):
        return 2 * self.height + 0.3

class Coat(Clothes):
    def __init__(self,size):
        self.size = size

    @property
    def consumption(self):
        return self.size/6.5 + 0.5

a = Suit(200)
print(a.consumption)

b = Coat(46)
print(b.consumption)