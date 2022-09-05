# 32. The following classes are implemented:
    
# • Vehicle
# • LandVehicle
# • AirVehicle

# Define a dispiay_info( ) method in the Vehicle class to display the class 
# name along with the value of the category attribute. 

# The method is supposed to work for all classes.

# For example, the following code:
# instances = [Vehicle(), LandVehtcle(), AirVehtcle()] for instance 
# in instances: print(instance)

# returns:
# Vehicle -> land vehicle
# LandVehicle
# land vehicle
# AirVehicle -> air vehicle

# Run the code below in response:
# instances = [Vehicle(), LandVehicle(), AirVehicle()] for instance 
# in instances: print(instance)

# Expected result: 
#     Vehicle -> land vehicle
#     LandVehlcle -> land vehicle 
#     AlrVehlcle -> air vehicle

class Vehicle:
    
    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'
        
    def display_info(self):
        print("{} -> category {}".format(self.__class__.__name__, self.category))
                                         
class LandVehicle(Vehicle):
    pass;

class AirVehicle(Vehicle):
    
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'

vehicles = [Vehicle(), LandVehicle(), AirVehicle()]        

[vehicle.display_info() for vehicle in vehicles]