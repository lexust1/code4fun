# 48. Implement a class called Car that sets the following instance attributes 
# when creating an instance:
# • brand
# • model
# • price
# • type_of_car, by default ‘sedan '

# Then create an instance named car with the given values:
# * brand = 'BMW
# • model = 'X3'
# • price = 200000
# • type_of_car = 'SUV'

# In response, print the value of the diet attribute of the car instance.
# Expected result:
# {'brand': 'BMW, 'model': 'X3', 'price': 200000, 'type_of_car': 'SUV'}

class Car:
    
    def __init__(self, brand, model, price, type_of_car = 'sedan'):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car
        
car = Car('BMW', 'X3', 200000, 'SUV')

print(car.__dict__)        

