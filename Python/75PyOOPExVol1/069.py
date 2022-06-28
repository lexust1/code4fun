# 69. A class called Pet is implemented that has two properties: name and 
# age (see below). Create an instance of the Pet class with the name pet and 
# attribute values respectively:
# • 'Max'
# •7

# Then try to modify the value of the age attribute to -10. If there is an 
# error, print this error message to the console. Use a try ... except ... 
# clause in your solution.

# Expected result:
# The value of age must be a positive integer.

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
        
        
        
pet = Pet('Max', 7) 
       
try:
    pet.age = -10
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)    