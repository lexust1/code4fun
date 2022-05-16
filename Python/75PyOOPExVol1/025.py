# Implement a class named Phone. 

# In the Phone class, define two class attributes with names:
# • brand
# • model

# and set their values to:
# • 'Apple'
# • ‘iPhone X'

# Then use the built-in functions getattr() and print () to display the values 
# of the given attributes of the Phone class to the console as shown below.

# Expected result: 
# Apple
# iPhone X

class Phone:
    brand = 'Apple'
    model = 'iPhone X'
    
print(getattr(Phone, 'brand'))
print(getattr(Phone, 'model'))    

