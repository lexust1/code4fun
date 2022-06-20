# You are given an odd-length array of integers, in which all of them are 
# the same, except for one single number.

# Complete the method which accepts such an array, and returns 
# that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3



def stray(arr):
    
    max_arr = max(arr)
    min_arr = min(arr)
    
    if arr[0] == arr[-1] and arr[0] == max_arr:
        return min_arr
    if arr[0] == arr[-1] and arr[0] == min_arr:
        return max_arr
    if arr[0] != arr[-1] and arr[0] == arr[1]:
        return arr[-1]
    if arr[0] != arr[-1] and arr[0] != arr[1]:
        return arr[0]
    
def stray(arr):
    return min(arr, key=arr.count)      
