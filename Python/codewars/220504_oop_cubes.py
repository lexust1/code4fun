# Hey Codewarrior!

# You already implemented a Cube class, but now we need your help again! 
# I'm talking about constructors. We don't have one. 
# Let's code two: One taking an integer and one handling no given arguments!

# Also we got a problem with negative values. Correct the code so negative 
# values will be switched to positive ones!

# The constructor taking no arguments should assign 0 to Cube's Side property.

# 1
class Cube:
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, _side=0):
        self._side = abs(_side)
        
    
    def get_side(self):
        """Return the side of the Cube"""
        return abs(self._side)

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side

# 2        
class Cube:
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side=0):
        self._side = side   
    
    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)        