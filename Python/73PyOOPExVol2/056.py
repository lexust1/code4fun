# 56. The Note class is given. 

# Implement a find( ) method that checks if a given word is in the note 
# (case insensitive). 

# The method should return True or False, respectively.

# Then create an instance named notel with the contents of the note: 
#     'Object Oriented Programming in Python.'

# On the note1 instance call the find() method to check if the note contains 
# the following words:
# 'python''
# Python'

# Print the result to the console. Expected result:
# True
# True

import datetime

class Note:
    
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
        
    def find(self, word):
        return word.lower() in self.content.lower()
        
        
        
note1 = Note ('Object Oriented Programming in Python.')

print(note1.find('Python'))        
print(note1.find('python')) 