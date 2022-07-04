class Item:

    NumPad = ''
    pay_rate = 0.8

    all = []

    def __init__(self, name, price, quan = 1400): # We can add Default value to any parameter
        # print(f"I want {quan} pieces of {name} of price {price}")
        
        self.__name = name #to print the parameters
        self.__price = price
        self.quan = quan

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_disc(self):
        self.__price = self.__price*Item.pay_rate

    def apply_inc(self, inc_val):
        self.__price += self.__price * inc_val

    def calcu(self):
        return self.__price*self.quan

    def __repr__(self): #use {self.__class__.__name__} to specificly mention the name of class 
        return f"{self.__class__.__name__} ('{self.__name}', '{self.__price}', '{self.quan}')" 

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f'''
        Hello Someone.
        We have {self.name} {self.quan} times.
        Regards, Shark
        '''
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

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
