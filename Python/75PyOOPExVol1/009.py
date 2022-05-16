# 9. Implement a function called stick( ) that takes any number of 
# bare arguments and return an object of type str being a concatenation 
# of all arguments of type str passed to the function with the '#' sign 
# (see below).

# Example:
# [IN]: stick('sport', 'summer', 4, True)
# [OUT]: 'sport#summer’

# As an answer call the stick( ) function in the following ways 
# (print the result to the console):
# • stick('sport', 'summer')
# • stick(3, 5, 7)
# stick(False, 'time'. True, 'workout', [], 'gym') Expected result:
# Sport#sumer
# time#workout#gym

def stick(*args):
    args = [el for el in args if isinstance(el, str) == True]
    return "#".join(args)
    
print(stick('1', '4', 'Call', 10))    
print(stick('sport', 'summer', 4, True))
print(stick(False, 'time', True, 'workout', [], 'gym')) 