# 40. The Book class is defined. 

# Implement a method named set_title() that sets an instance attribute 
# named title. 

# Before setting the value, check if it's an object of str type, 
# if not raise a TypeError with the following message:

# 'The value of the title attribute must be of str type.'

# Then create an instance of the Book class named book and set the title 
# attribute to ' inferno ' using the set_title() method.

# In response, print the value of the title attribute of the book instance.

# Expected result: 
# Python OOPS Exercises
# class Book: 
#     language = 'ENG'
#     is_ebook = True

class Book:
    language = 'Eng'
    is_ebook = True
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("The value of the title attribute must be of str type.")
        self.title = title
     
        
book = Book()

book.set_title('Inferno') 
print(book.title)

#book.set_title(11)            