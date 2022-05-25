# 41. The Book class is defined. 

# A method called set_title( ) was implemented that allows you to set 
# an instance attribute called title. 

# Create an instance of the Book class named book. 
# Then, using the try ... except ... clause, 
# try using the set_title()method to set the value of the title attribute 
# to False . 
# In case of a TypeError , print the error message to the console.

# Expected result:
# The value of the title attribute must be of str type.
# class Book: 
#     language = 'ENG' 
#     is_ebook = True
# def set_title(self, value):
#     if not isinstance(value, str):
#         raise TypeError('The value of the title attribute must be of str ' 'type.')
#         self.title = value

class Book:
    language = 'Eng'
    is_ebook = True
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("The value of the title attribute must be of str type.")
        self.title = title

book = Book()

try:
    book.set_title(False)
except TypeError as error:
    print(error)
        
