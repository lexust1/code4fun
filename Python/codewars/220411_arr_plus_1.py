# Given an array of integers of any length, return an array that 
# has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# For example the array [2, 3, 9] equals 239, adding one would 
# return the array [2, 4, 0].

# [4, 3, 2, 5] would return [4, 3, 2, 6]

def up_array(arr):
    if not arr:
        return None
    if any([1 if el < 0 or el > 9 or isinstance(el, int) != 1 else 0 
            for el in arr]) == 1:
        return None
    return [int(di) for di in str(int(''.join([str(el) for el in arr])) + 1)]
        
        
       
 # if [None for el in arr if el < 0 or el > 9 or isinstance(el, int) != 1]