# 74. A class named Circle is given. 

# Add a property called area (read-only) to the class that calculates the area 
# of a circle with a given radius. 

# This property should only be computed at first reading or after 
# modifying the radius attribute. 

# To do this, also modify the way of setting the value of the
# radius attribute in the _init_( ) method. 

# Make sure that the value of the area attribute isrecalculated after changing 
# the radius attribute. 

# Then create an instance named circle with radius=3 .

# In response, display the value of the perimeter attribute to 
# the console (round the result to four decimal places).

# Expected result: 18.8496

import numpy as np

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        self._perimeter = None
        
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
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * np.pi * self._radius
        return self._perimeter    
    
circle = Circle(3)
print(circle.__dict__)
print("Perimeter: {}".format(np.around(circle.perimeter, 4)))   
print(circle.__dict__)