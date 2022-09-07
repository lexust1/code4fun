# 59. Implementations of the Note and Notebook class are given.

# Implement a method called search() in the Notebook class that allows you to 
# return a list of notes containing a specific word (passed as an argument to 
# the method, case insensitive). 

# You can use the Note.find method for this.

# Create an instance of the Notebook class named notebook. 
# Then, using the new_note() method add notes to the notebook with the following content:
# • 'Big Data'
# • 'Data Science'
# • 'Machine Learning'

# In response, call the search() method on the notebook instance looking for 
# notes that contain the Word 'data' .

# Expected result:
# [Note(content='Big Data'), Note(content='Data Science')]

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
        
    def search(self, value):
        return [note for note in self.notes if note.find(value)]
        
notebook = Notebook()
notebook.new_note('Big Data')
notebook.new_note('Data Science')
notebook.new_note('Machine Learning')
print(notebook.search('data')) 