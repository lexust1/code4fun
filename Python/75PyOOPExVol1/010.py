# 10. Implement a function called dispiay_info() which prints the name of 
# the company (as shown below) and if the user also passes an argument named 
# price , it prints the price (as shown below).

# Example I:
# [IN]: dlsplay_info(company='Amazon')
# Company name: Apple

# Example II:
# [IN]: display_info(company='Amazon', price=1140) 
# Company name: Amazon 
# Price: $ 1140

# In response, call display_info() as shown below: 
# display_info(company='CD Projekt', price=100)

# Expected result:
# Company name: CD Projekt 
# Price: $ 100

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

        
display_info(company='Amazon', price=1140)         