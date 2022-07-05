# 2. Using the classmethod class (do it in the standard way) implement a class 
# named Person that has a class method named show_details() which displays the 
# following text to the console:
    
# 'Running from Container class.'

# Try to pass the class name using the appropriate attribute of the Person 
# class.
 
# In response, call the show_details() class method.

# Expected result:
# 'Running from Container class.'

class Person:
    
    @classmethod
    def show_details(cls):
        print("Running from {} class.".format(cls.__name__))
        
Person.show_details()    
        