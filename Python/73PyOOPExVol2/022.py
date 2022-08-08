# An implementation of the Vector class is given. 

# Implement the _f loordiv_ ( ) special method
# to do the integer division of Vector instances (division by coordinates). 
# For simplicity, assume that the user divides vectors of the same length and 
# the coordinates of the second vector are not zeros. 
# Then create two instances of this class:
# • vl = Vector(4, 2)
# • v2 = Vector(-1, 4)
# and perform an integer division for these vectors. 

# Print the result to theconsole.
# Expected result: (-4, 0)

class Vector:
    
    def __init__(self, *components):
        self.components = components
        
    def __repr__(self):
        return "Vector{}".format(self.components)
    
    def __str__(self):
        return "Vector components: {}".format(self.components)
    
    def __add__(self, other):
        components = tuple(comp1 + comp2 for comp1, comp2 in 
                           zip(self.components, other.components))
        return components
    
    def __sub__(self, other):
        components = tuple(comp1 - comp2 for comp1, comp2 in
                           zip(self.components, other.components))
        return Vector(*components)
    
    def __mul__(self, other):
        components = tuple(comp1 * comp2 for comp1, comp2 in
                           zip(self.components, other.components))
        return Vector(*components)
    
    def __truediv__(self, other):
        components = tuple(comp1 / comp2 for comp1, comp2 in 
                           zip(self.components, other.components))
        return Vector(*components)
    
    def __floordiv__(self, other):
        components = tuple(comp1 // comp2 for comp1, comp2 in
                           zip(self.components, other.components))
        return Vector(*components)
        

    
v1 = Vector(4, 2)
v2 = Vector(-1, 4)

v3 = v1 // v2
print(v3)