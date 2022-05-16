# Classy Extensions
# Classy Extensions, this kata is mainly aimed at the new JS ES6 Update 
# introducing extends keyword. You will be preloaded with the Animal class, 
# so you should only edit the Cat class.
# Task
# Your task is to complete the Cat class which Extends Animal and replace 
# the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
# The name attribute is passed with this.name (JS), @name (Ruby) 
# or self.name (Python).


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name+' makes a noise.'

class Cat(Animal):
    def speak(self):
        return self.name+' meows.'
        
        
        
        