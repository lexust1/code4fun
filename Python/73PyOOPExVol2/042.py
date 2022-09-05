# 42. The following classes are defined. 

# Add the _init_( ) method to the Workerclass to set all the attributes from 
# the Person and Department classes.

# Then create an instance of the Worker class passing the following arguments:
# • 'John'
# • 'Doe'
# • 30
# • 'Information Technology’
# • 'IT'
# In response, print the value of the _dict_ attribute of this instance.
# •
# Expected Result:
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 
#  'dept_name': 'Information Technology', 'short_dept_name': 'IT'}

class Person:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Department:
   
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name

class Worker(Person, Department):
    
    def __init__(self, first_name, last_name, age, dept_name, short_dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name, short_dept_name)

worker = Worker('John', 'Doe', 30, 'Information Technology', 'IT')

