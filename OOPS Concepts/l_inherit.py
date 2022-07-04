from numpy import append
from c_init import Item

class phone(Item):

    def __init__(self, name, price, quan, disc = 0.45):
        
        self.name = name
        self.price = price
        self.quan = quan
        self.disc = disc

phone1 = phone('Shark A', 1000, 100)
print(phone1.calcu())
phone2 = phone('Shark z', 1000, 150)
print(phone2.calcu())
