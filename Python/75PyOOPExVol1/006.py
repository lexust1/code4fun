# 6. Import the built-in datetime module and display the namespace of 
# this module (sorted alphabetically) as given below.

# Tip: Use the _dict_ attribute of the datetime module.

# Expected result: 
#     MAXYEAR
#     MINYEAR 
#     _builtlns_ 
#     _cached_ 
#     _doc_ 
#     _file_ 
#     _loader_ 
#     _name_ 
#     _package_ 
#     _spec_ 
#     date 
#     datetime
    
import datetime

print(datetime.__dict__)

