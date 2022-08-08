# 23. The following Doc class is implemented for storing text documents. 
# Implement the _add_ ( ) special method to add Doc instances with a space 
# character.

# Example:
# [IN]: docl = Doc('Object')
# [IN]: doc2 = Doc('Oriented') 
# [IN]: print(docl + doc2)
# [OUT]: Object Oriented
# Then create two instances of the Doc class for the following documents:
# • 'Python'
# • '3.8'

# In response, print the result of adding these instances to the console. 

# Expected result:
# Python 3.8

class Doc:
    
    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return "Doc{}".format(self.string)

    def __str__(self):
        return "Doc object keeps: {}".format(self.string)

    def __add__(self, other):
        return Doc(self.string + " " + other.string)

doc1 = Doc('Python')
doc2 = Doc('3.8') 

doc3 = doc1 + doc2
print(doc3)        