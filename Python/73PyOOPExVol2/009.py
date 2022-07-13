# The Book class is implemented. Add a _repr_( ) method to the Book class 
# that represents an instance of this class (see below).

# Then create an instance of the class named book 1 passing the following 
# arguments:
    
# • title= ‘Python Object Oriented Programming Exercises Volume 2'
# • author='Edcorner Learning'

# In response, print the instance book1 to the console.

# Expected result:
# Book(title=' Python Object Oriented Programming Exercises Volume 2', 
#      author='Edcorner Learning')

import uuid

# No __repr__
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()
        
    # def __repr__(self):
    #     return "Book('{}', '{}')".format(self.title, self.author)
        
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

book1 = Book('Python Object Oriented Programming Exercises Volume 2', 
             'Edcorner Learning')        

print(book1)

 # __repr__
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()
        
    def __repr__(self):
        return "Book('{}', '{}')".format(self.title, self.author)
        
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


        
    
book1 = Book('Python Object Oriented Programming Exercises Volume 2', 
             'Edcorner Learning')        

print(book1)