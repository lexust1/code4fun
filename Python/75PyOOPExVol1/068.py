# 68. A class called Pet is implemented that has two properties: 
# name and age (see below). 
    
# Add validation to the age property at the stage of object creation 
# and attribute modification:
# • the value of the age attribute must be an int type, otherwise raise 
# a TypeEmor with the following message:
# 'The value of age must be of type int.’

# the value of the age attribute must be positive, otherwise raise valueEmor 
# with the following message:
# 'The value of age must be a positive integer.'

# Then try to create an instance of the Pet class named pet and set the 
# following values:
# • 'Max'
# • 'seven'

# If there is an error, print an error message to the console. 
# Use a try ... except ... clause your solution.

# If there is an error, print an error message to the console. 
# Use a try ... except . . clause in your solution.

# Expected result:
# The value of age must be of type Int.

class Pet:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("The value of age must be of type int.")
        if value <= 0:
            raise ValueError("The value of age must be a positive integer.")
        self._age = value
        
try:
    pet = Pet('Max', 'seven')
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)    
            
        