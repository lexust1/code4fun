# 35. The Book class is defined. Create an instance of the Book class 
# named book. 
# Display the value of the _dict_ attribute for the book instance. 

# Then assign two attributes to the book instance:
# • author to the Value 'Dan Brown'
# • title to the value ' Inferno '

# In response, display the _dict_ attribute for the book instance again. 

# Expected result:
# {}
# {'author': 'Dan Brown','title','Inferno'}
# class Book: 
    # language = 'ENG' 
    # is_ebook = True

class Book:
    language = 'Eng'
    is_ebook = True

book = Book()

print(book.__dict__)

book.author = 'Dan Brown'
book.title = 'Inferno'

print(book.__dict__)
