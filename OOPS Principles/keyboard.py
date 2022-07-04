from b_oops import Item

class Keyboard(Item):
    pay_rate = 0.7 #overriding in the child class is legal
    def __init__(self, name, price, quan):
        super().__init__(
            name, price, quan
        )
