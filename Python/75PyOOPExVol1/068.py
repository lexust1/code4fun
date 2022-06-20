# 68. A class called Pet is implemented that has two properties: 
# name and age (see below). 
    
# Add validation to the age property at the stage of object creation 
# and attribute modification:
# • the value of the age attribute must be an int type, otherwise raise 
# a TypeEmor with the following message:
# 'The value of age must be of type int.’

# the value of the age attribute must be positive, otherwise raise valueEmor 
# with the following message:
# 'The value of age must be a positive integer.'

# Then try to create an instance of the Pet class named pet and set the 
# following values:
# • 'Max'
# • 'seven'

# If there is an error, print an error message to the console. 
# Use a try ... except ... clause your solution.

# If there is an error, print an error message to the console. 
# Use a try ... except . . clause in your solution.

# Expected result:
# The value of age must be of type Int.

class Pet:
    
    def __init__(self, name, age):
        