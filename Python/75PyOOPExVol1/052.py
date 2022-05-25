# 52. A class called Laptop was implemented. 

# Then, an instance of the Laptop class named laptop was created with 
# the following arguments:
# • 'Acer'
# • 'Predator'
# • 5490

# In response, print the value for each instance attribute (on a separate line) 
# of the laptop instance as shown below.

# Expected result: 
#     brand -> Acer 
#     model -> Predator 
#     price -> 5490

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
        
laptop = Laptop('Acer', 'Predator', 5490)

[print(key, "->", value) for key, value in laptop.__dict__.items()]     

print('brand ->', laptop.brand)   
print('model ->', laptop._model)
print('price ->', laptop._Laptop__price)