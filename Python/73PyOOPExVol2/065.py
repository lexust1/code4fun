# 65. Create a class named StringListOnly that extends the built-in list class. 

# Modify the behavior of the append () method so that only objects of str type 
# can be added to the list. 

# If you try to add a different type of object raise TypeE rror with message:
# 'Only objects of type str can be added to the list.'

# Then create an instance of the StringListOnly class and add the following 
# objects with the append() method:
# 'Data' 'Science'

# In response, print result to the console.Expected result: ['Data', 'Science']

class StringListOnly(list):
    
    def append(self, string):
        if isinstance(string, str) is True:
            super().append(string)
        else:
            raise TypeError('Only a string object can be added to list')

lst = StringListOnly()
lst.append(10)
lst.append('Python')

print(lst)