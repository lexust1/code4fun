# 37. The Book class is defined. 
# Two instances of the Book class named book_1 and book_2 was created. 
# Then the instance attributes were assigned to these objects 
# (using the dot notation), respectively:
# book_1: 
#     author = 'Dan Brown'
#     title = 'Inferno' 
# book_2:
# title = 'The Da Vinci Code' 
# year_of_publishment = 2003

# Then a books list was created. Create a loop to list all the attributes 
# of the book_l and book_2 instances with their values as shown below 
# (separate each instance with a line of 30 1 - ' characters as shown below).

#  Expected result:
# author -> Dan Brown
# title -> Inferno 
# ------------------------------ 
# author -> Dan Brown
# title -> The Da Vinci 
# Code year_of_publishment -> 2003
# ------------------------------ 

class Book:
    language = 'Eng'
    is_ebook = True
    
book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

list_of_books = [book_1, book_2]    

[print(key, "->", values) for key, values in book_1.__dict__.items()]
print('-' * 30)
[print(key, "->", values) for key, values in book_2.__dict__.items()]
print('-' * 30)

[[print(key, "->", values) for key, values in book.__dict__.items()] 
 for book in list_of_books]
