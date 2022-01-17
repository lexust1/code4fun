# 6. 
# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers. 

# Sample data : 3, 5, 7, 23

# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

seq_num = input("Input a sequence of comma-separated numbers: ")

lst_num = seq_num.split(',')
tpl_num = tuple(lst_num)

print("A list of numbers: ", lst_num)
print("A tuple of numbers: ", tpl_num)

