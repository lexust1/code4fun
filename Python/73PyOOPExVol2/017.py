# An implementation of the Vector class is given. 

# Implement the _add_( ) special method to
# add Vector instances (by coordinates). 

# For simplicity, assume that the user adds vectors of the same length. 
# Then create two instances of the Vector class:
# vl = Vector(4, 2)
# v2 = Vector(-l, 3)
# and perform the addition of these vectors. 
# Print the result to the console. 

# Expected result:
# (3,5)

class Vector:
    
    def __init__(self, *components):
        self.components = components
        
    def __str__(self):
        return "Vector components: {}".format(self.components)

    def __repr__(self):
        return "Vector{}".format(self.components)
    
    def __len__(self):
        return len(self.components)
    
    def __add__(self, other):
        components = tuple(comp1 + comp2 for comp1, comp2 in 
                           zip(self.components, other.components)) 
        return Vector(*components)

v = Vector(1, 2, 3)    
print(str(v))
print(repr(v))   
print(len(v)) 

v1 = Vector(4, 2)
v2 = Vector(-1, 3)

v3 = v1 + v2
print(v3)