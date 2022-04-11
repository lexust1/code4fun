# If　a = 1, b = 2, c = 3 ... z = 26

# Then l + o + v + e = 54

# and f + r + i + e + n + d + s + h + i + p = 108

# So friendship is twice stronger than love :-)

# The input will always be in lowercase and never be empty.

import string

def words_to_marks(s):
    return sum([string.ascii_lowercase.index(ch) + 1 for ch in s])


def words_to_marks(s):
    return sum([ord(ch) - 96 for ch in s])