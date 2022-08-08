# An implementation of the Vector class is given. Implement the _sub_ () 
# special method that subtracts Vector instances (by coordinates). 

# For simplicity, assume that the user subtracts vectors of the same length. 

# Then create two instances of this class:
# • vl = Vector(4, 2)
# • v2 = Vector(-l, 3)and perform the subtraction of these vectors. 

# Print the result to the console. 

# Expected result:
# (5, -1)

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

    
v1 = Vector(4, 2)
v2 = Vector(-1, 3)

v3 = v1 - v2
print(v3)