# 12. Implement a class named Vector which, when creating an instance takes 
# any number of arguments (vector coordinates in n-dimensional space - 
# without any validation) and assign it to an attribute named components.

# Then implement the _repr_( ) special method to display a formal 
# representation of Vector as shown below:
    
# [IN]: vl = Vector(l, 2) 
# [IN]: print(vl)[Out]: Vector(l, 2)

# Create a vector from the R3 space with coordinates: (-3,4,2) and assign it 
# to the variable v7. 

# In response, print the variable vl to the console.

# Expected result: 
#     Vector(-3, 4, 2)

class Vector:
    
    def __init__(self, *components):
        self.components = components
        
    def __repr__(self):
        return "Vector{}".format(self.components)
    
v1 = Vector(-3, 4, 2)

print(v1)    