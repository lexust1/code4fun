# 33. A class named OnlineShop was defined with the class attributes 
# set accordingly:
# • Sector to the Value 'electronics'
# • sector_code to the value 'ele'
# • is_public_company to the value False

# Implement a function (class callable attribute) named get_sector() 
# that returns the value of the sector attribute of OnlineShop class. 
# You only need to implement this function.

# class OnlineShop:
# sector = 'electronics' sector_code = 'ELE' is_public_company = False

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ele'
    is_public_company = False

def get_sector():
    return print(OnlineShop.sector)    

get_sector()

