# 59. Implement a class named Person that has one protected instance 
# attribute named first_name. 

# Next, implement a method get_first_name( ) which reads the value 
# of the firstname protected attribute. 

# Then, using the get_first_name( ) method and the property class 
# (do it in the standard way) create a property named firstname 
# (read-only property).

# Create an instance of the Person class and set the firstname attribute 
# to ' john ' . 

# Print the value of the firstname attribute of this instance to the console.

# Expected result: 
# John

class Person:
    
    def __init__(self, first_name):
        self._first_name = first_name
        
    def get_first_name(self):
        return self._first_name
    
    first_name = property(fget=get_first_name)
    
person = Person('John')

print(person.first_name)
print(person._first_name)    