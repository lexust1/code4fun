# 47. Implement a class called Car that sets the following instance attributes 
# when creating an instance:
# • brand
# • model
# • price
# • type_of_car, by default ‘sedan '

# Then create an instance named car with the given values:
# • brand = 'Opel'
# • model = 'Insignia'
# • price = 115000

# In response, print the value of the _dict_ attribute of the car instance.

# Expected result:
# {'brand': 'Opel', 'model': 'Insignia', 'price': 115000, 'type_of_car': 'sedan'}

class Car:
    
    def __init__(self, brand, model, price, type_of_car = 'sedan'):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car

car = Car('Opel', 'Insignia', 115000)

print(car.__dict__)        

car = Car('Opel', 'Insignia', 115000, 'pickup')

print(car.__dict__)        