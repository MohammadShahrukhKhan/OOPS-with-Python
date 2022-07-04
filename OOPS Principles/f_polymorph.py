''' Polymorphism principle '''

from keyboard import Keyboard

item1 = Keyboard('MyKeyboard', 1000, 2)

item1.apply_disc()
#you have the control over how much 
# discount do you have to give

print(item1.price)
