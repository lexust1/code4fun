# 26. The following Doc class is implemented for storing text documents. 

# Implement the _it_( )
# special method to compare Doc instances. 

# A class instance is 'smaller1 than another instance when the string attribute 
# is shorter.

# Example:
# [IN]: docl = Doc('Finance') 
# [IN]: doc2 = Doc('Education')
# [IN]: print(docl < doc2) 
# [OUT]: True

# Then create two instances of the Doc class for the following documents:
# • 'sport'
# • 'activity'

# and assign to the variables: 
# doc1
# doc2

# In response, print the result of comparing these instances 
# (perform doc1 < doc2 ).

# Expected result: True

class Doc:
    
    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return "Doc{}".format(self.string)

    def __str__(self):
        return "{}".format(self.string) 

    def __add__(self, other):
        return Doc(self.string + '' + other.string)  
    
    def __lt__(self, other):
        return len(self.string) < len(other.string)
        
doc1 = Doc('sport')
doc2 = Doc('activity')

print(doc1 < doc2)    
    