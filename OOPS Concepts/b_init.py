class Item:

    def __init__(self, name, price, quan):
        print(f"I want {quan} {name} of price {price}")
        
        self.name = name #to print parameters
        self.price = price
        self.quan = quan


Item1 = Item("iPhones", '$1500', 12)
print(Item1.name) #self
print(Item1.price)
print(Item1.quan)

Item2 = Item("MacBooks", "$3500", 12)
print(Item2.name)
print(Item2.price)
print(Item2.quan)
