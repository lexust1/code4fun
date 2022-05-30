# 54. An implementation of the Laptop class is given. 
# Implement a method in the Laptop class called dispay_private_attrs( )
#  that displays the names of all private attributes of the instance. 
 
#  Then create an instance with the given arguments:
# 'Acer' 
# 'Predator' 
# 'AC-100' 
# 5490

# 0.2
# and assign it to the variable laptop. 

# In response, call display_protected_attrs( ) on the laptop instance.

# Expected result: 
# _model
# _code

class Laptop:
    
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
        
    def display_protected_attrs(self):
        return [print(attr) for attr in self.__dict__ if
                attr.startswith("_") 
                and not attr.startswith("_{}".format(self.__class__.__name__))]

laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2) 

laptop.display_protected_attrs()      