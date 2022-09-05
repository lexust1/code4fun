# 33. A Vehicle class is given that has three instance attributes:
# • brand
# • color
# • year

# Create a Car class that inherits from Vehicle class. 

# Next, override the _init ( ) method so
# that the Car class in the constructor takes four arguments:
# • brand 
# * color 
# * year
# * horsepower
# and set them appropriately as instance attributes. 

# Don't use super () in this case. 

# Then create following instances:
# • with the name vehicle and the attribute values: 'BMW', 'red', 2020
# • with the name car and the attribute values: 'BMW', 'red', 2020, 300

# In response, print the value of the _dict_ attribute of the vehicle and 
# car instances.

# Expected result:
    
# {'brand': ' BMW’, 'color': 'red', 'year': : 2020}
 
# {1 brand' : ' BMW’, 'color': 'red', 'year': : 2020, 'horsepower': 300}

# class Vehicle:
#     def __init__(self, brand, color, year): 
#         self.brand = brand
#         self.color = color
#         self.year = year
        
class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

class Car(Vehicle):
    
    def __init__(self, brand, color, year, horsepower):
        self.brand = brand
        self.color = color
        self.year = year
        self.horsepower = horsepower
        
vehicle = Vehicle('BMW', 'red', 2020)

car = Car('BMW', 'red', 2020, 300)

print(vehicle.__dict__)
print(car.__dict__)        

        