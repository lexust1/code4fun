# 28. Implement a class named OnlineShop with 
# the class attributes set appropriately:
    
# • Sector to the Value 'electronics'
# • sector_code to the value 'ele'
# • is_public_company to the value False

# Then, using dot notation, add a class attribute called country 
# and set its value to 'usa' . In response, print the user-defined 
# OnlineShop class attribute names as shown below.

# Expected result:
# ['sector', 'sector_code', 1is_public_company','country']

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ele'
    is_public_company = False

OnlineShop.country = 'USA'

attrs = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]    

print(attrs)

