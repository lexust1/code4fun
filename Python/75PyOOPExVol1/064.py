# 64. Implement a class named Pet that has one protected instance attribute 
# name. 

# Then implement a method name( ) which reads the value of the protected 
# name attribute.

# Create a property name (read-only) using the @property decorator.

# Create an instance of the Pet class named pet and set name attribute 
# to 'Max' . 

# In response, print the contents of the _dict_
# attribute of this instance.Expected result: {'_name': 'Max'}


class Pet:
    
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
pet = Pet('Max')
print(pet.__dict__)    