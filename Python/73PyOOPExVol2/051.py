# 51. The people list is given. Sort the objects in the people list ascending 
# by age. 

# Then print the name and age to the console as shown below.

# Expected result: 
# Alice-> 19 
# Tom ->25
# Mike -27
# John -> 29 

class Person:
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
people = [Person('Tom', 25), Person('John', 29), 
          Person('Mike', 27), Person('Alice', 19)]

people.sort(key=lambda person: person.age)

[print(person.name, '->', person.age) for person in people]