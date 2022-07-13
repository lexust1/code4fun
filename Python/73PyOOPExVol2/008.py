# 8. Complete the implementation of the Book class. 

# In the _init_ ( ) method, set the bare attributes of the instance with names:
# • title
# • author
# • book_id

# Set the instance book_id attribute using the uuid module. 

# Exactly theuuid. uuid4( ) function from this module. 

# An example of using this function:
# import uuid 
# str(uuid.uuid4().fields[-1])[: 6]
# Returns a 6-element string. This will be the value of the book_id attribute.


# Using the above code, create a static method of the Book class 
# (use the @staticmethod decorator) called get_id() L which will generate 
# a 6- digit str object (the value of the bookjd field).

# Then create an instance of the class named bookl with the following arguments:
    
# • title=' Python Object Oriented Programming Exercises Volume 2'
# • author='Edcorner Learning'

# In response, print all the _dict_ attribute keys of book1 to the console.

# Expected result:
# dict_keys(['book_id', 'title', 'author'])

import uuid

# w/ static method
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()
        
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    
book1 = Book('Python Object Oriented Programming Exercises Volume 2', 
             'Edcorner Learning')    

print(book1.__dict__)
        


# w/o static method
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = str(uuid.uuid4().fields[-1])[:6]
        

    
book1 = Book('Python Object Oriented Programming Exercises Volume 2', 
             'Edcorner Learning')    

print(book1.__dict__)