# 2. Using the built-ins module import the sum( ) function. Then display 
# its documentation of this function. Call the function on the list below 
# and print the result to the console.
# [-4, 3, 2]

# Expected result:
# Help on built-in function sun in nodule built-ins:
# sum(iterable, /, start=0)
# Return the sun of a 'start' value (default: 0) plus an iterable of numbers
# When the Iterable is empty, return the start value.
# This function is intended specifically for use with numeric values and 
# may reject non-numeric types. 1

import builtins

help(builtins.sum)


# print(sum.__doc__)

print(sum([-4, 3, 2]))