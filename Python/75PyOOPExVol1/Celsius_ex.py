# Python @property decorator
# In this tutorial, you will learn about Python @property decorator; 
# a pythonic way to use getters and setters in object-oriented programming.

# Python programming provides us with a built-in @property decorator which 
# makes usage of getter and setters much easier in Object-Oriented Programming.

# Before going into details on what @property decorator is, 
# let us first build an intuition on why it would be needed in the first place.


## 1 ##

# Class Without Getters and Setters
# Let us assume that we decide to make a class that stores the temperature in 
# degrees Celsius. It would also implement a method to convert the temperature 
# into degrees Fahrenheit. One way of doing this is as follows:
    
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature  = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32        
    
# We can make objects out of this class and manipulate the temperature 
# attribute as we wish:    
    
# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

# Whenever we assign or retrieve any object attribute like temperature as 
# shown above, Python searches it in the 
# object's built-in __dict__ dictionary attribute.    

human.__dict__

# Therefore, man.temperature internally becomes man.__dict__['temperature'].


## 2 ##

# Using Getters and Setters
# Suppose we want to extend the usability of the Celsius class defined above. 
# We know that the temperature of any object cannot reach below -273.15 
# degrees Celsius (Absolute Zero in Thermodynamics)

# Let's update our code to implement this value constraint.

# An obvious solution to the above restriction will be to hide the 
# attribute temperature (make it private) and define new getter and setter 
# methods to manipulate it. This can be done as follows:

# Making Getters and Setter methods
class Celsius:

    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return self.get_temperature() * 1.8 + 32             
    
    # getter method
    def get_temperature(self):
        return self._temperature
    
    # setter method
    def set_temperature(self, temperature):
        if temperature < -273.15:
            raise ValueError ("Temperature below -273.15 is not possible.")
        self._temperature = temperature

# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())

# This update successfully implemented the new restriction. 
# We are no longer allowed to set the temperature below -273.15 
# degrees Celsius.

# Note: The private variables don't actually exist in Python. 
# There are simply norms to be followed. The language itself doesn't 
# apply any restrictions.

human._temperature = -300
human.get_temperature()

# However, the bigger problem with the above update is that all 
# the programs that implemented our previous class have to modify their 
# code from obj.temperature to obj.get_temperature() and all expressions 
# like obj.temperature = val to obj.set_temperature(val).

# This refactoring can cause problems while dealing with hundreds of thousands 
# of lines of codes.

# All in all, our new update was not backwards compatible. This is where 
# @property comes to rescue.



## 3 ##

# The @property Decorator
# In Python, property() is a built-in function that creates and returns a 
# property object. The syntax of this function is:

# property(fget=None, fset=None, fdel=None, doc=None)
# where,

# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)

# As seen from the implementation, these function arguments are optional. 
# So, a property object can simply be created as follows.

# >>> property()
# <property object at 0x0000000003239B38>
# A property object has three methods, getter(), setter(), and deleter() 
# to specify fget, fset and fdel at a later point. This means, the line:

# temperature = property(get_temperature,set_temperature)
# can be broken down as:

# # make empty property
# temperature = property()
# # assign fget
# temperature = temperature.getter(get_temperature)
# # assign fset
# temperature = temperature.setter(set_temperature)
# These two pieces of codes are equivalent.
    
class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature() * 1.8 + 32             
    
    # getter method
    def get_temperature(self):
        print("Getting value ...")
        return self._temperature
    
    # setter method
    def set_temperature(self, temperature):
        print("Setting value ...")
        if temperature < -273.15:
            raise ValueError ("Temperature below -273.15 is not possible.")
        self._temperature = temperature
        
    temperature = property(fget=get_temperature, fset=set_temperature)    

human = Celsius(37)    


# Programmers familiar with Python Decorators can recognize that the above 
# construct can be implemented as decorators.

# We can even not define the names get_temperature and set_temperature as 
# they are unnecessary and pollute the class namespace.

# For this, we reuse the temperature name while defining our getter and 
# setter functions. Let's look at how to implement this as a decorator:

class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32             
    
    @property
    def temperature(self):
        print("Getting value ...")
        return self._temperature
    
    @temperature.setter
    def temperature(self, temperature):
        print("Setting value ...")
        if temperature < -273.15:
            raise ValueError ("Temperature below -273.15 is not possible.")
        self._temperature = temperature
        
    

human = Celsius(37)        

print(human.temperature)
print(human._temperature)

print(human.to_fahrenheit())

print(human.temperature)
print(human._temperature)

print(human.__dict__)

cold = Celsius(-300)


# The above implementation is simple and efficient. It is the recommended way 
# to use property.


# Change the name "temparature" foor @propertry decorator



class Celsius:

    def __init__(self, temperature = 0):
        self.name_of_property = temperature

    def to_fahrenheit(self):
        return (self.name_of_property * 1.8) + 32             
    
    @property
    def name_of_property(self):
        print("Getting value ...")
        return self._temperature
    
    @name_of_property.setter
    def name_of_property(self, temperature):
        print("Setting value ...")
        if temperature < -273.15:
            raise ValueError ("Temperature below -273.15 is not possible.")
        self._temperature = temperature
        
human = Celsius(37)           
 
print(human.name_of_property)
print(human._temperature)

print(human.to_fahrenheit())

print(human.name_of_property)
print(human._temperature)

print(human.__dict__)

cold = Celsius(-300)        
        


