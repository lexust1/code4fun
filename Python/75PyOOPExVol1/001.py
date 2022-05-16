# 1. The stock_info( ) function is defined. Using the appropriate attribute 
# of the stock_info( ) function, display the names of all arguments to 
# this function to the console.

# An example of calling the function: 

# print(stock_info('ABC', 'USA', 115, '$')) 
# Company: ABC
# Country: USA
# Price: $ 115

# Tip: Use the code attribute of the function. 

# Expected result:   
# ('company', 'country', 'price', 'currency')

def stock_info(company, country, price, currency):
    info = (
    "Company: {company}\n"
    "Country: {country}\n"
    "Price: {currency} {price}\n"
    .format(company = company, 
            country = country, 
            price = price, 
            currency = currency)
    ) 
    return info

print(stock_info('ABC', 'USA', 115, '$'))

