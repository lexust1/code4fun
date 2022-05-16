# 20. Define two empty classes named:
    
# • Model
# • View

# Then create two instances (one for each class):
# • model for the Model class
# • view for the View class

# Using the built-in function isinstance( ) check whether the model and 
# view objects are instances of the Model class. 

# Print the result to the console.
# Expected result: 
# True
# False

class Model:
    pass

class View:
    pass

model = Model()

view = View()

print(isinstance(model, Model))

print(isinstance(view, Model))