# 5. A display_info() function was implemented. This function has 
# an incorrectly implemented internal update_counter( ) function. 
# Correct the implementation of this function so that you can modify 
# non- local variables: counter and dot_counter from the internal function
# update_counter() .
# I
# n response, call dispiay_info( ) with the number_of_updates argument 
# set to 10. 

# Tip: Use the nonlocal statement.

# Expected result:
# 110
# ..........

# def display_info(number_of_updates=1): 
#     counter = 100
#     dot_counter = ''
#     def update_counter():
#         counter += 1
#         dot_counter += '.'

# [update_counter() for _ in range(number_of_updates)] 
# print(counter)
# print(dot_counter)

def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''
    
    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'
     
    [update_counter() for i in range(number_of_updates)]
        
    print(counter)
    print(dot_counter)
               

display_info(number_of_updates=10)
