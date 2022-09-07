# 64. Create a class named CustomDict that extends the built-in diet class. 

# Add a method named is_any_str_vaiue() that returns a boolean value:
# • True in case the created dictionary contains at least one value of str type
# • otherwise False.

# Example I:
# [IN]: cd = CustonDict(python=’mid')
# [IN]: print(cd.ls_any_str_value()) 
# returns:
# [OUT]: True

# Example II:
# [IN]: cd = CustomDict(price=119.99) 
# [IN]: print(cd.ls_any_str_value())

# returns:
# [OUT]: False

# You only need to implement the CustomDict class.

class CustomDict(dict):
    
    def is_any_str_value(self):
        
        return [True if isinstance(self[key], str) else False for key in self][0] 
        

cd = CustomDict(python='mid')  
print(cd.is_any_str_value())

cd = CustomDict(price=119.99)  
print(cd.is_any_str_value())