# An implementation of the Vector class is given. Implement the _truediv( ) 
# special method
# which allows you to divide Vector instances (division by coordinates). 
# For simplicity, assume that the user divides vectors of the same length and 
# the coordinates of the second vector are not zeros. 

# Then create two instances of this class:
# • vl = Vector(4, 2)
# • v2 = Vector(-l, 4)
# and perform the division of these vectors. Print the result to the console.
# Expected result: (-4.0, 0.5)

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

    
v1 = Vector(4, 2)
v2 = Vector(-1, 4)

v3 = v1 / v2
print(v3)