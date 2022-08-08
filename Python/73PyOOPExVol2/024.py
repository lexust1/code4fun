# The following Hashtag class is implemented for storing text documents 
# - hashtags. 

# Implement the _add_ () special method to add (concatenate) Hashtag instances 
# using a space character as shown below (take into account the appropriate 
# number of ■ # ■ characters at the beginning of the new object).

# Example:
# [IN]: hashtagl = Hashtag('sport')
# [IN]: hashtag2 = Hashtag('travel1') 
# [IN]: print(hashtagl + hashtag2) 
# [OUT]: »sport »travel

# Then create three Hashtag instances for the following text documents: 
# • python
# • developer
# • oop

# In response, print the result of adding these instances.
# Expected result: #python #developer #oop

class Hashtag:
    
    def __init__(self, string):
        self.string = '#' + string
        
    def __reps__(self):
        return "Hashtag{}".format(self.string)
    
    def __str__(self):
        return "Object's hashtags: {}".format(self.string)
    
    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)

hashtag1 = Hashtag('python')
hashtag2 = Hashtag('developer')
hashtag3 = Hashtag('oop')

hashtags = hashtag1 + hashtag2 + hashtag3
print(hashtags)