from click import argument


class Item:

    NumPad = ''

    def __init__(self, name: str, price: int, quan): # We can add Default datatype too
        print(f"I want {quan} pieces of {name} of price {price}")
        # Run Validations to received arguments 
        assert price > 1000, "price is low" #if the values are less then the given assertions then this message is shown
        assert quan > 1000, "price is less"

        # assign to self objects 
        self.name = name #to print the parameters
        self.price = price
        self.quan = quan

    def calcu(self):
        return self.price*self.quan


Item1 = Item("iPhones", 1500, 1400)
print(Item1.name) #self
print(Item1.price)
print(Item1.quan)
print(Item1.calcu())

Item2 = Item("MacBooks", 3500, 1400)
Item2.NumPad = False
print(Item2.name)
print(Item2.price)
print(Item2.quan)

print(Item2.NumPad)

print(Item2.calcu())


