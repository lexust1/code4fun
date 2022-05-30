# 60. Implement a class named Person that has two instance protected 
# attributes named first_name and lastname, respectively. 

# Then implement methods named get_first_name() and get_last_name( ), 
# which reads the protected attributes: firstname and lasLname.

# Then, using the get_first_name() and get_last_name() methods and the 
# property class (do it in the standard way) create two properties named 
# firstname and lastname (read-only properties).

# Create an instance of the Person class and set the following attributes: 
# • firstname to the value 'John'
# • lastname to the value 'Dow'

# Print the value of the firstname and last_name attribute of this instance 
# to the console.

# Expected result: 
# John
# Dow

class Person:
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    first_name = property(fget=get_first_name)
    last_name = property(fget=get_last_name)
    
person = Person('John', 'Dow')

print(person.first_name)
print(person._first_name)

print(person.last_name)
print(person._last_name)

