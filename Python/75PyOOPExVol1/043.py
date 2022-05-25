# 43. A class called Laptop was implemented.
# Implement a method in the Laptop class called display_instance_attrs() 
# that displays the names of all the attributes of the Laptop instance.

# Then create an instance named laptop with the given attribute values:
# • brand =
# • model =
# • price =

# In response, call display_instance_attrs() method on the laptop instance. 

# Expected result:
# brand model price
# 'Dell' 'Inspiron' 3699

# class Laptop:
# def __init__(self, brand, model, price):
# self.brand = brand self.model = model self.price = price

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def display_instance_attrs(self):
        return self.__dict__.keys()
        
laptop = Laptop('Dell', 'Inspiron', 3699)        



[print(key) for key in laptop.display_instance_attrs()]
