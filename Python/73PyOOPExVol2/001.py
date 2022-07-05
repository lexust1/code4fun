# 1. Using the classmethod class (do it in the standard way) implement a class 
# named Person that has a class method named show_details() which displays the 
# following text to the console:
    
# 'Running from Person class.'

# Try to pass the class name using the appropriate attribute of the Person 
# class. 

# In response, call the show_details() class method.

# Expected result:
    
# Running from Person class.

class Person:
    
    def show_details(cls):
        print("Running from {} class".format(cls.__name__))
        
    show_details = classmethod(show_details)
    
Person.show_details()    