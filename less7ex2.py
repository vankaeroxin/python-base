from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def textile(self):
        return self.param


class Coat(Clothes):
    def textile(self):
        return f'Расход ткани для пальто: {self.param/6.5 + 0.5:.2f}'


class Suit(Clothes):
    def textile(self):
        return f'Расход ткани для костюма: {2 * self.param  + .3:.2f}'


coat = Coat(10)
suit = Suit(1.88)

print(coat.textile())
print(suit.textile())
