# 51. Implement a class called Laptop that sets the following instance 
# attributes when creating an instance:
# • brand as a bare instance attribute
# • model as a protected attribute
# • price as a private attribute

# Then create an instance named laptop with the following arguments:
# • 'Acer' 
# 'Predator'
# • 5490
# In response, print the value of the _dict_ attribute of the laptop instance. 

# Expected result:
# {'brand': 'Acer', '_model': 'Predator', '_Laptop__price': 5490}

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
        
laptop = Laptop('Acer', 'Predator', 5490)

print(laptop.__dict__)        

