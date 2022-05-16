# 32. A class named OnlineShop was defined with the class attributes 
# set accordingly:
# • Sector to the Value 'electronics'
# • sector_code to the value 'ele'
# • is_public_company to the value False

# Outside of the class, implement a function called describe_attrs() 
# that displays the names of all user- defined class attributes and their 
# values as shown below. 
# In response, call the
# describe_attrs() function.
# Expected result: sector -> electronics sector_code -> ELE
# is_public_conpany -> False


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ele'
    is_public_company = False
    
def describe_attrs():
    [print(attr, '->', value) for attr, value in OnlineShop.__dict__.items() 
     if not attr.startswith('_')]   
    
    
describe_attrs()    