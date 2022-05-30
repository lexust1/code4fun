# 55. Implement a class called Laptop which in the init ( ) method sets 
# the value of the price protected attribute that stores the price of 
# the laptop (without any validation). 

# Then implement a method to read that attribute named get_price() and 
# a method to modify that attribute named set_price( ) without validation as well.

# Then create an instance of the Laptop class with a price of 3499 and 
# follow these steps:
# • using the get_price( ) method print the value of the price protected 
# attribute to the console
# • using the set_price( ) method, set the value of the price protected 
# attribute to 3999
# • using the get_price( ) method print the value of the price protected 
# attribute to the console

# Expected result: 
# 3499
# 3999

class Laptop:
    
    def __init__(self, price):
        self._price = price
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
        
laptop = Laptop(3499)

print(laptop.get_price())

laptop.set_price(3999)

print(laptop.get_price())        