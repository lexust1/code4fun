# 21. Two empty classes are defined:
    
# • Model
# • View

# Three objects were created (object1, object2, object3).

# Using the built-in function is instance ( ) check whether object1, object2 
# and object3 are instances of the Model class or of the View class. 


# Print the result to the console.

# Expected result: 
# True
# False
# False


class Model:
    pass

class View:
    pass

object1 = Model()
object2 = [Model(), Model()]
object3 = {}

print(isinstance(object1, (Model, View)))

print(isinstance(object2, (Model, View)))

print(isinstance(object3, (Model, View)))