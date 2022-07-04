class Item:

    pay_rate = 0.45

    def __init__(self, name, price, quan):
        print(f"I want {quan} {name} of price {price}")
        
        self.name = name #to print parameters
        self.price = price
        self.quan = quan

    def apply_disc(self):
        self.price = self.price*self.pay_rate


Item1 = Item("iPhones", 1500, 12)
print(Item1.name) #self
print(Item1.price)
print(Item1.quan)
Item1.apply_disc() # applied to Item1
print(Item1.price) # value changed


Item2 = Item("MacBooks", 3500, 12)
Item2.pay_rate = 0.3
print(Item2.name)
print(Item2.price)
print(Item2.quan)
Item2.apply_disc() 
print(Item2.price) 




