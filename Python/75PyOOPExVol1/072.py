# 72. Implement a class named Circle that will have the protected instance 
# attribute radius - the radius of the circle (readable and 
# modifiable property). Use the @property decorator.

# Then create an instance named circle with radius=3.

# In response, display the _dict_ attribute of circle instance. 

# Expected result:
# {'_radius': 3}

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        
circle = Circle(3)

print(circle.__dict__)        