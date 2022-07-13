# 11. The Person class is implemented. 

# Add a special method _str_ () to return an informal
# representation of an instance of the Person class.

# Example:
# [IN]: person = Person('Mike', 'Smith')
# [IN]: print(person)First name: Mike Last nane: Smith

# Then create an instance named person with the following values:
# • fname = 'Edcorner’
# • lname = 'Learning'

# In response, print the person instance to the console.

# Expected result:
# First name: Edcorner
# Last name: Learning

class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
                      
    def __repr__(self):
        return "Person(fname='{}', lname='{}')".format(self.fname, self.lname)
            
    def __str__(self):
        return  "First name: {}\nLast name: {}".format(self.fname, self.lname)

person = Person('Edcorner', 'Learning')
print('Print:')
print(person)
print('rep:')
print(repr(person))
print('str:')
print(str(person))