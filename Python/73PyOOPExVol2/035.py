# 35. The Vehicle and Car classes are listed below. 

# Extend the dispiay_attrs() method in the Car class so that the following 
# information is displayed before displaying the attributes: 
#     ' calling from class: Car' and then the rest of the attributes with 
#     their values. Use super () for this. 
    
# For example, for the Car class:
# car = Car('BMW', 'red', 2020, 190) car.dlsplay_attrs() returns:
#     Calling fron class: 
#         Car brand -> BMW 
#         color -> red
#         year -> 2020
#         horsepower -> 190
# Then create an instance of the class Car named car with the attribute values: 
#     ' BMW’ 'black', 2018, 260
# In response, call display_attrs( ) on the car instance.
# Expected result: 
#     Calling from class: 
#         Car brand -> BMW 
#         color -> black 
#         year -> 2018 
#         horsepower -> 260

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
        
    def display_attrs(self):
        [print("Calling from class: {} -> {}".format(attr, value)) 
          for attr, value in self.__dict__.items()] 
        
    
car = Car('Opel', 'black', 2018, 160)
car.display_attrs() 