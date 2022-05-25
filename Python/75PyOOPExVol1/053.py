# 53. An implementation of the Laptop class is given. 
# Implement a method in the Laptop class called dispiay_private_attrs( ) 
# that displays the names of all private attributes of the instance. 

# Then create an instance with the given arguments:
# • 'Acer'
# • 'Predator'
# • 'AC-100'
# • 5490
# • 0.2
# and assign it to the variable laptop. In response, call 
# dispiay_private_attrs() on the laptop instance.

class Laptop:
    
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
        
    def display_private_attrs(self):
        return [print(attr) for attr in self.__dict__ if 
                attr.startswith("_{}__".format(self.__class__.__name__))]
        
laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)        

laptop.display_private_attrs()

