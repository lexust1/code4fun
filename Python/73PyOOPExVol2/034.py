# The Vehicle and Car classes are listed below. 

# Implement a method named dispiay_attrs() in the base class Vehicle, 
# which displays the instance attributes and their values. 

# For example, for the Vehicle class:
# vehicle = Vehlcle('BMW', 'red', 2020) 
# vehicle.dlsplay_attrs() 
# brand -> BMW
# color -> red
# year -> 2020

# And for the Car class:
# car = Car(‘BMW’, 'red', 2020, 190) c
# ar.dlsplay_attrs()
# brand -> BMW c
# olor -> red
# year -> 2020
# horsepower -> 190

# Then create an instance of the Car class named car with the attribute values: 
    
#  Opel ', 'black', 2018, 160
 
# In response, call dispiay_attrs( ) on the car instance. 

# Expected result:
# brand -> Opel
# color -> black 
# year -> 2018 
# horsepower -> 160

class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        
    def display_attrs(self):
        [print("{} -> {}".format(attr, value)) for attr, value in 
         self.__dict__.items()]      

        
class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower        
    
car = Car('Opel', 'black', 2018, 160)
car.display_attrs() 