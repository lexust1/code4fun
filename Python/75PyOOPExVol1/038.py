# 38. The Book class is defined. 

# A list books_data is also given. 

# books_data = [{'author': 'Dan Brown', 'title': 'Inferno'}, 
#               {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishnent': 2003}]

# Based on this data, create two instances of the Book class, where 
# the instance attributes will be the keys from the given dictionaries 
# (books_data list) with their corresponding values.

# In response, print the _dict_ attributes of the objects to the console 
# as shown below.

# Expected result:
# {'author': 'Dan Brown', 'title': 'Inferno'}
# {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003} 

# class Book:
# language = 'ENG'
# is_ebook = True 
# books_data = [
# {'author': 'Dan Brown', 'title': 'Inferno'},
# {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003} ]

class Book:
    language = 'Eng'
    is_ebook = True
    
book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books_data = [book_1, book_2]    

[print(book.__dict__) for book in books_data]


    