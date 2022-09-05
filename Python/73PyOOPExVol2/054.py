# 54. Implement a class called Note that describes a simple note. 

# When creating Note objects, an instance attribute called content will be set
# with the contents of the note. 

# Also add instance attribute called creationjime that stores the creation time 
# (use the given date format: '%m-%d- %Y %H:%M:%S' ).

# Next, create two instances of the Note class named notel and note2, 
# and assign the following contents: 
# 'My first note.'
# 'My second note.'

import datetime

class Note:
    
    def __init__(self, content):
         self.content = content
         self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
         
note1 = Note('My first note.') 
note2 = Note('My second note.')

        