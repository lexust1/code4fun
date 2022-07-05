# 5. A class named Person is given. 

# Modify the _init() method so that you can set two instance attributes: 
#     firstname and lastname (bare attributes, without any validation).

# Create two instances of the Person class. 

# Then call the count_instances() class method and print result to the console.

# Expected result: 2

class Person:
    
    instances = []
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Person.instances.append(self)
        
    @classmethod 
    def count_instances(cls):
        return len(Person.instances)
    
person1 = Person('Kevin', 'Lee')
person2 = Person('John', 'Smith')

print(Person.count_instances())    
print(person1.count_instances())