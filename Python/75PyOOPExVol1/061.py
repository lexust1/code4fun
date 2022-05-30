# 61. Implement a class named Person that has two instance protected 
# attributes named first_name and lastname, respectively. 

# Then implement methods named get_first_name() and get_last_name( ) ,
#  which reads the protected attributes: firstname and lasLname.

# Then, using the get_first_name() and get_last_name() methods and the 
# property class (do it in the standard way) create two properties named 
# firstname and lastname (read-only properties).

# Create an instance of the Person class and set the first_name attribute to
#  ■ Dohn ' . 
 
# Then, using the set_first_name() method, Set new value 'Mike' .
 
# In response, print the value of the first_name attribute to the console.
# Expected result: Mike

class Person:
    
    def __init__(self, first_name):
        self._first_name = first_name
        
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name  
        
    first_name = property(fget=get_first_name, fset=set_first_name)

person = Person('Dohn')

print(person.first_name)

person.set_first_name('Mike')

print(person.first_name)    