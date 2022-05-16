# 15. The implementation of the Container class is given:
# class Container:
# """This is a Container class."""

# Display all _dict_ attribute keys of the Container class to the console. 

# Expected result:
# dict_keys(['__module__', '__dict__', '__weakref__', '__doc__'])
# class Container:
# """This is a Container class."""

class Container:
    """This is a Container class"""
    
print(Container.__dict__)
print(Container.__dict__.keys())    