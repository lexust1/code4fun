# 13. An implementation of the Vector class is given. 
# Implement the _str_() display an informal representation of a Vector 
# instance as shown below:
    
# [IN]: vl = Vector(l, 2)
# [IN]: print(vl)
# [Out]: (1, 2)
# special method to

# Create a vector from the RA3 space with coordinates: (-3,4,2) and assign it 
# to the variable vl.

# In response, print the variable vl to the console.

# Expected result: (-3, 4, 2)

class Vector:
    
    def __init__(self, *components):
        self.components = components
    
    def __repr__(self):
        return "Vector{}".format(self.components)

    def __str__(self):
        return "{}".format(self.components)
    
v1 = Vector(-3, 4, 2)

print(v1)

print(repr(v1))

print(str(v1))    

        