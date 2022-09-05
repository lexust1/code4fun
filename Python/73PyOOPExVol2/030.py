# 30. The following classes are implemented: • Container• PlasticContainer
# • MetalContainer
# • CustomContainer

# Using the issubciassQ built-in function, check if the classes: 
# PlasticContainer
# MetalContainer
# • CustomContainer
# are subclasses of Container class. 

# Print the result to the console as shown below:
# True 
# True
# False

class Container:
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

class CustomContainer:
    pass

print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))
