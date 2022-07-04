''' Encapsulation principle '''

from a_oops import Item

item1 = Item('MyItem', 750)
 
# item1.price = -900

item1.apply_inc(0.2)
item1.apply_disc()

print(item1.price)
