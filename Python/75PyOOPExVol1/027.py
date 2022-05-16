# 27. A class named Laptop is defined below. 

# Using the setattr( ) built-in function modify the value of attributes:
# • brand to 'Acer'
# • model to 'Predator'

# In response, using the built-in function getattr() and print() .
# print the values of the brand and model attributes to the console 
# as shown below.

# Expected result:
#  brand: Acer 
#  model: Predator

class Laptop:
    brand = 'Asus'
    model = 'Strix'

setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(Laptop.brand)
print(Laptop.model)


    