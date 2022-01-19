# 2. 
# Write a Python program to get the Python version you are using.


import sys

py_ver = "Python version: {ver}".format(ver=sys.version)
py_ver_info = "Version info: {ver_info}".format(ver_info=sys.version_info)

print(py_ver)
print(py_ver_info)