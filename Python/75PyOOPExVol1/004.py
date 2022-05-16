# The following global variables are given:
# • counter
# • dot_counter
# and incorrectly implemented update_counters ( ) function. 
# Correct the implementation of the update_counters ( ) function so that you 
# can modify the values of the given global variables from this function. 
# Then call update_counters() 40 times.
# In response, print the value of the counter and dot_counter global variables 
# to the console as shown below.

# Tip: Use the global statement.

# Expected result:
# 40

# counter = 0 
# dot_counter = ''
# def update_counter():
#   counter += 1 
#   dot_counter += '.'

counter = 0
dot_counter = ''

def update_counter():
    global counter
    counter +=1
    global dot_counter
    dot_counter += '.'
    
[update_counter() for i in range(40)]    

print(counter)
print(dot_counter)

