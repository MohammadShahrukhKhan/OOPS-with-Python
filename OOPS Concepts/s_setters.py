class Item:

    NumPad = ''

    all = []

    def __init__(self, name, price, quan = 1400): # We can add Default value to any parameter
        print(f"I want {quan} pieces of {name} of price {price}")
        
        self.__name = name #to print the parameters
        self.price = price
        self.quan = quan

        Item.all.append(self)

    @property
    #property decorator = read only attribute
    def name(self):
        return self.__name #encapsulation

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('Name is too long')
        else:
            self.__name = value

    def calcu(self):
        return self.price*self.quan

    def __repr__(self): #use {self.__class__.__name__} to specificly mention the name of class 
        return f"{self.__class__.__name__} ('{self.__name}', '{self.price}', '{self.quan}')" 

# Item1 = Item("iPhones", 1500)
# print(Item1.name) #self
# print(Item1.price)
# print(Item1.quan)
# print(Item1.calcu())

# Item2 = Item("MacBooks", 3500)
# Item2.NumPad = False
# print(Item2.name)
# print(Item2.price)
# print(Item2.quan)

# print(Item2.NumPad)

# print(Item2.calcu())

# print(Item.all)
