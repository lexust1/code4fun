# Given an integer as input, can you round it to the next (meaning, "higher") 
# multiple of 5?

# Examples:

# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).

# You can assume that all inputs are valid integers.
import math

def round_to_next5(n):
    return math.ceil((n / 5)) * 5  


def round_to_next5(n):
    return n + (5 - n) % 5;