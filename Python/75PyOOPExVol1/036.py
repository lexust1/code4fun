# 36. The Book class is defined. Create two instances of the Book class 
# named book_1 and book_2. 

# Then assign instance attributes to these objects (using dot notation) 
# as follows:
# to object book_1:
# author = 'Edcorner Learning'
# title = 'Python Programming Exercises' 

# to object book_2:
# author = 'Edcorner Learning' 
# title = 'Python OOPS Exercises'
# year_of_publishment = 2021

# In response, print the value of the _dict_ attribute of book_1 and book_2. 

# Expected result:
# {'author': 'Edcorner Learning', 'title': 'Python Programming Exercises'}
# {'author': 'Edcorner Learning', 'title': 'Python OOPS Exercises', 'year_of_publishment': 2021}

# class Book: 
#     language = 'ENG'
#     is_ebook = True

class Book:
    language = 'ENG'
    is_ebook = True

book1 = Book()
book2 = Book()

book1.author = 'Edcorner Learning'
book1.title = 'Python Programming Exercises'

book2.author = 'Edcorner Learning'
book2.title = 'Python OOPS Exercises'
book2.year_of_publishment = 2021

print(book1.__dict__)
print(book2.__dict__)    