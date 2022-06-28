# 73. A class named Circle is given. Add a property called area (read-only) 
# to the class that calculates the area of a circle with a given radius. 

# This property should only be computed at first reading or after modifying 
# the radius attribute. 

# To do this, also modify the way of setting the value of the
# radius attribute in the _init_()method.

# Make sure that the value of the area attribute is recalculated after changing 
# the radius attribute. 

# Then create an instance named circle with radius=3 .

# Solution:
# In response, display the value of the area attribute to the console 
# (round the result to four decimal places).

# Expected result: 
#     28.2743
import numpy as np

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        
    @property
    def area(self):
        if self._area is None: 
            self._area = np.pi * self._radius * self._radius
        return self._area 
    
circle = Circle(3)
print(circle.__dict__)
print("Area: {}".format(np.around(circle.area, 4)))   
print(circle.__dict__)