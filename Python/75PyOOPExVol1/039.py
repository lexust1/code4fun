# 39. The Book class is defined. 

# Implement a method called set_title() that allows you to set an instance 
# attribute called title (without validation). 

# Then create an instance of the Book class named book and set the title 
# attribute to ' inferno' using the set_title( ) method.

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
        self.title = title
        
book = Book()
book.set_title('Python OOP Exercises')
print(book.title)

