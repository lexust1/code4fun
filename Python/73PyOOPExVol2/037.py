# 37. Simple classes with the following structure are implemented: 
#     • Container
#     • TemperatureControlledContainer 
#     • RefrigeratedContainer 
 
#  Using the built-in issubclass() function, check if:
# • TemperatureControlledContainer is a class derived from Container
# • RefrigeratedContainer is a class derived from TemperatureControlledContainer
# • RefrigeratedContainer is a class derived from Container

class Container:
    pass

class TemperatureControlledContainer(Container):
    pass

class RefrigeratedContainer(TemperatureControlledContainer):
    pass

print(issubclass(TemperatureControlledContainer, Container))
print(issubclass(RefrigeratedContainer, TemperatureControlledContainer))
print(issubclass(RefrigeratedContainer, Container))
      