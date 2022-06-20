# 65. Implement a class named Pet that has two protected instance attributes: 
    
# name and age, respectively. 

# Next implement the methods: name() and age(), which reads the value of 
# the protected attributes: name and age.

# Using the @property decorator, create properties: name and age, 
# respectively (read-only properties).

# Create an instance of the Pet class named pet and set the name attribute 
# to ' Max ' and age to

# In response, print the contents of the _dict_ attribute of pet instance 
# to the console.

# Expected result:
#  {'_name': 'Max', '_age': 5}
 
class Pet:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

pet = Pet('Max', 5)

print(pet.__dict__)        

