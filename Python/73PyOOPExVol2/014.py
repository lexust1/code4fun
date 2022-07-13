# 14. An implementation of the Vector class is given. Implement the _len_ ( ) 
# special method to return the number of vector coordinates.

# Example:
# [IN]: vl = Vector(3, 4, 5) 
# [IN]: print(len(vl)) 
# [Out]: 3

# Create a vector from the RA3 space with coordinates: (-3,4,2) and assign it 
# to the variable v7. In response, print the number of coordinates of this 
# vector using the built-in len() function.

# Expected result: 3

class Vector:
    
    def __init__(self, *components):
        self.components = components
        
    def __repr__(self):
        return "Vector{}".format(self.components)
    
    def __str__(self):
        return "{}".format(self.components)
    
    def __len__(self):
        return len(self.components)
    
v1 = Vector(-3, 4, 2)    

print(len(v1))