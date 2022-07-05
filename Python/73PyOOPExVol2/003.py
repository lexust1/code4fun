# 3. The Container class is given. Create an instance of this class named 
# container and call the show_details( ) method from this instance.

# Expected result:
    
# Running from Container class.

class Container:
    
    @classmethod
    def show_details(cls):
        print("Running from {} class.".format(cls.__name__))
        
container = Container()
container.show_details()    
        