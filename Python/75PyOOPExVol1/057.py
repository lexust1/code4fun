# 57. A class called Laptop was implemented. 

# The _init_( ) method sets the value of the price
# protected attribute that stores the price of the laptop 
# (without any validation).

# Create an instance of the Laptop class with a price of 3499 and 
# try to set the price to -3000 using the set_price( ) method. 

# If an error is raised, print the error message to the console. 

# Use a try ... except ... clause in your solution.

# Expected result:
# The price attribute must be a positive int or float value.

class Laptop:
    
    def __init__(self, price):
        self._price = price
        
    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self._price = price
        else:
            raise TypeError("The price attribute must be a positive int or float value.")
            
laptop = Laptop(3499)

print(laptop.get_price())         

#laptop.set_price( -3000)

try:
    laptop.set_price(-3000)
except TypeError as error:
    print(error)
        
print(laptop.get_price())       