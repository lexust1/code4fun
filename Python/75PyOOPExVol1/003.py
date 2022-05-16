# 3. A global variable counter is given with an incorrectly implemented 
# update_counter() function. Correct the implementation of 
# the update_counter ( ) function so that you can modify the counter variable 
# from this function. Then call the update_counter ( ) function.

# Tip: Use the global statement.
# Expected result: 2

counter = 1
print(counter)
def update_counter():
    #print(counter)
    global counter
    print(counter)
    counter += 1
    
    
update_counter()    
print(counter)