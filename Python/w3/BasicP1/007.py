# 7. 
# Write a Python program to accept a filename from the user and 
# print the extension of that. 

# Sample filename : abc.java

# Output : java

fn = input("Input a filename with extension: " )
ext = fn.split('.')[-1]

print("The file extension:", ext)

