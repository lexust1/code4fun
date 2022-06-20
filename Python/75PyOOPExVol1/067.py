# 67. Implement a class named Pet that has one protected instance attribute 
# name. 

# Then, using the @property decorator, create a property name 
# (property to read and modify, without validation).

# Create an instance of the Pet class with the name pet and attributes:
# • name = 'Max'
# • age = 5

# Print the _dict_ attribute of the pet instance to the console. 

# Then modify the attributes using the dot notation:
# • name to the value 'Tom’
# • age to the value 8

# Again, print the _dict_ attribute of the pet instance to the console again.

# Expected result:
# {'_name': 'Max', '_age1 :5}
# {'_name': 'Ton', '_age1 :8}

class Pet:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
         
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age        
        
pet = Pet('Max', 5)
print(pet.__dict__)

pet.name = 'Tom'
pet.age = 8
print(pet.__dict__)        
        
        