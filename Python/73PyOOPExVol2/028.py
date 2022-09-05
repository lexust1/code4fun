# 28. The Book class is given. 

# Implement the _str _() method to display an informal
# representation of a Book instance (see below).

# Example:
# [IN]: bookl = Book('Python OOPS Vol2', 'Edcorner Learning’) 
# [IN]: print(bookl)
# [OUT]: Book ID: 214522 | Title: Python OOPS Vol2 | Author: Edcorner Learning

# Then create an instance named book with arguments:
# • title= ‘Python OOPS Vol2’
# • author='Edcorner Learning’

# In response, print the instance to the console. 

# Expected result:
# Book ID: 1234 | Title: Python OOPS Vol2 | Author: Edcorner Learning

# Note: The Book ID value may vary.

import uuid

class Book:
    
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author
        
    def __repr__(self):
        return "Book(title='{}', author='{}')".format(self.title, self.author)
    
    def __str__(self):
        return "Book ID: {} | Title: {} | Author: {}".format(self.book_id, 
                                                             self.title, 
                                                             self.author)

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

book = Book('Python OOPS Vol2', 'Edcorner Learning')    

print(book)

print(str(book))   

print(repr(book)) 