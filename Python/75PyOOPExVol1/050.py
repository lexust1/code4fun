# 50. A class called Laptop was implemented.

# Try to create values:
# an instance named laptop with the given attribute
# • brand=
# • model
# • price =

# Note that in this case the value of the price attribute is passed 
# as a str type. 
# In
# 'Acer'
# = 'Predator'
# '5900'case of error, print the error message to the console 
# (use the try ... except ... clause).

# Expected result:
# The price attribute must be a positive int or float.

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else: 
            raise TypeError("The price attribute must be a positive int of float.")         
            
try: 
    laptop = Laptop('Acer', 'Predator', '5900')
except TypeError as error:
    print(error)            
        
        