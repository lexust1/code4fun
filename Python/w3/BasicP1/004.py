# 4.
# Write a Python program which accepts the radius of a circle from the user 
# and compute the area. 
#
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


import math

r = input("Enter the radius of a circle: ")
S = math.pi * float(r) ** 2 
print ("The area of a circle: {area}".format(area=S))