from c_init import Item

item3 = Item('MyItem', 750)
 
''' shows AttributeError: can't set attribute 'meme' '''
# item3.name = 'Otherwise'

print(item3.name)
