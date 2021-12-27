"""
1.
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

           
# 1st method

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")

# 2nd method

var_str = (
    "Twinkle, twinkle, little star,\n"
    "\tHow I wonder what you are!\n"
    "\t\tUp above the world so high,\n"
    "\t\tLike a diamond in the sky.\n"
    "Twinkle, twinkle, little star,\n"
    "\tHow I wonder what you are!"
    )

print(var_str)
