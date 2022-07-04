from numpy import append
from c_init import Item

class phone(Item):

    # all = [] #works even after being removed

    def __init__(self, name, price, quan, disc = 0.45):
        # call to super function to have access to all attributes / methods
        super().__init__(name, price, quan)  
        
        self.disc = disc

        # phone.all.append(self)

phone1 = phone('Shark A', 1000, 100)
print(phone1.calcu())
phone2 = phone('Shark z', 1000, 150)
print(phone2.calcu())

print(phone.all)








