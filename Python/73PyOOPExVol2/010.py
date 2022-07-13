# 10. Define a Person class that takes two bare attributes: 
#     fname (first name) and lname (last name).
    
# Then implement the _repr_ ( ) special method to display a formal 
# representation of the Person object as shown below:
    
# [IN]: person = Person('John', 'Doe')
# [IN]: print(person)
# [OUT]: Person(fname='John', lname=’Doe’)

# Create an instance of the Person class with the given attributes:
    
# fname = 'Mike' 
# lname = 'Smith'

# and assign it to the variable person. 

# In response, print the person instance to the console.

# Expected result: Person(fname='Mike’, lname='Smith')

class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __repr__(self):
        return "Person(fname='{}', lname='{}')".format(self.fname, self.lname)

person = Person('John', 'Doe')
print(person)
        
person1 = Person('Mike', 'Smith')
print(person1)