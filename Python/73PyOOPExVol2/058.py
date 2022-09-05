# 58. Implementations of the Note and Notebook class are given. 

# Implement a method named dispiay_notes( ) in the Notebook class to display 
# the content of all notes of the notes instance attribute to the console.

# Create an instance of the Notebook class named notebook. T
# hen, using the new_note() method add two notes to the notebook with the 
# following content:
# • 'My first note.'
# • 'My second note.'

# In response, call dispiay_notes() method on the notebook instance.

# Expected result:
#     My first note. 
#     My second note.
    
import datetime

class Note:
    
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
        
    def __repr__(self):
        return "Note(content={})".format(self.content)
        
    def find(self, word):
        return word.lower() in self.content.lower()
        
class Notebook:

    def __init__(self):
        self.notes = []
        
    def new_note(self, content):
        self.notes.append(Note(content))  
        
    def display_notes(self):
        [print(nt.content) for nt in self.notes]     
        
notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
notebook.display_notes()     