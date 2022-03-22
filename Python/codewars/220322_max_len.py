# You are given two arrays a1 and a2 of strings. Each string is composed with 
# letters from a to z. Let x be any string in the first array and y be any 
# string in the second array.

# Find max(abs(length(x) − length(y)))

# If a1 and/or a2 are empty return -1 in each language except in Haskell 
# (F#) where you will return Nothing (None).

# Example:
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", 
#       "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13
# Bash note:
# input : 2 strings with substrings separated by ,
# output: number as a string

def mxdiflg(a1, a2):
    
    if a1 and a2:
        len_a1 = [len(el) for el in a1]
        len_a2 = [len(el) for el in a2]

        max1 = abs(max(len_a1) - min(len_a2))
        max2 = abs(max(len_a2) - min(len_a1))
        
        return max(max1, max2)
    
    else:
        
        return -1
    
def mxdiflg(a1, a2):
    
    if a1 and a2:
        return max(
        abs(len(max(a1, key=len)) - len(min(a2, key=len))),
        abs(len(max(a2, key=len)) - len(min(a1, key=len))))
    else:
        return -1
    
        

# def mxdiflg(a1, a2):
    
#     len_a1 = [len(el) for el in a1]
    
#     len_a2 = [len(el) for el in a2]
    
#     return max(max(len_a1) - min(len_a2), max(len_a2) - min(len_a1));