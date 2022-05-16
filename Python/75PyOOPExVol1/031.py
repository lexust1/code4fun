# 31. A class named OnlineShop was defined with the class attributes 
# set accordingly:
# • Sector to the Value 'electronics'
# • sector_code to the value 'ele'
# • is_public_company to the value False

# Display all user-defined OnlineShop class attribute names with their values 
# as shown below.

# Expected result: 
#     sector -> electronics 
# sector_code -> ELE
# etc
    
    

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ele'
    is_public_company = False
    


[print(attr, '->', value) for attr, value in OnlineShop.__dict__.items() 
 if not attr.startswith('_')] 


