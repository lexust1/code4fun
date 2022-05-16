# 23. Two empty classes are defined:

# • Model
# • View

# Using the built-in function issubclassQ check if the classes 
# Model and View are derived classes (subclasses) of the built-in object class.

# Expected result: 
# True
# True

class Model:
    pass

class View:
    pass 

print(issubclass(Model, object))
print(issubclass(View, object))