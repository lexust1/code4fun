# 38. Simple classes with the following structure are implemented: 
#     • Container
#     • TemperatureControlledContainer
#     • RefrigeratedContainer
    
# The TemperatureControlledContainer class inherits from the Container 
# class and the RefrigeratedContainer class inherits from 
# TemperatureControlledContainer.

# Add a class attribute called temp_range to the TemperatureControlledContainer 
# class that stores the tuple (-25.0, 25.0) , and to the RefrigeratedContainer 
# class add a class attribute with the same name and value (-25.0, 5.0) .:
    
# Then, using the getattr( ) function, read the value of the tempjange 
# attribute of the RefrigeratedContainer class and print to the console.

# Expected result: (-25.0, 5.0)

class Container:
    pass

class TemperatureControlledContainer(Container):
    temp_range = (-25, 25)
    

class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25, 0)
    
print(getattr(RefrigeratedContainer, 'temp_range'))  
print(getattr(TemperatureControlledContainer, 'temp_range'))

print(RefrigeratedContainer.__dict__) 
print(TemperatureControlledContainer.__dict__)


