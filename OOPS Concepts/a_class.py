class item:
    name = ""
    price = ""
    quan = ""
    pay_rate = 0.45
  
    def calcu_tot_price(self, x, y):
        return x*y
        
item1 = item() # Creating an Instance
item1.name = "toffee"
item1.price = 2
item1.quan = 7

print(item1.calcu_tot_price(item1.price, item1.quan))
print(item1.name)
print(item.pay_rate)
print(item1.pay_rate)

print(item.__dict__) # gives all attributes at class level
print(item1.__dict__) # gives all attributes at instance level


