# 63. A class named Person was implemented.

# Implement the del_first_name() method to remove the firstname protected 
# attribute.

# Then, Using the methods get_first_name() , set_first_name() , 
# del_first_name() and the property class (do this in the standard way) 
# create property named firstname (properties to read, modify and delete).

# Create an instance of the Person class named person and assign the value 
# Tom1 to firstname. 

# Use the del_first_name() method to delete the firstname attribute of 
# the person instance. 

# Display the _dict_attribute of the person instance to the console.
# Expected result: {}

class Person:
    
    def __init__(self, first_name):
        self._first_name = first_name
        
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def del_first_name(self):
        del self._first_name

    first_name = property(fget=get_first_name,
                          fset=set_first_name,
                          fdel=del_first_name)

person = Person('Tom')

print(person.__dict__)

person.del_first_name()

print(person.__dict__)
        