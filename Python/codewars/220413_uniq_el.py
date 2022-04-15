# There is an array with some numbers. All numbers are equal except for one. 
# Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique

def find_uniq(arr):
    max_el = max(arr)
    min_el = min(arr)
    if max_el == arr[0] and max_el == arr[1]:
        return min_el
    elif max_el == arr[0] and max_el != arr[1] and max_el == arr[2]:
        return min_el
    elif max_el != arr[0] and max_el == arr[1] and max_el == arr[2]:
        return min_el
    else:
        return max_el;
