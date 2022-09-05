# 43. The following classes are defined. 

# Display the MRO - Method Resolution Order for the Worker class.

# Note: The solution that the user passes is in a file named exercise.py, 
# while the checking code (which is invisible to the user) is executed from 
# a file named evaluate.py from the level where the classes are imported. 

# Therefore, instead of the name of the module
# _main_ , the response will be the name of the module in which this class is 
# implemented, in this case exercise .

# Expected result:
# [<class 'exercise.Worker’>, <class 'exercise.Person'>, <class'exercise.Departnent’, <class 'object’>]

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

print(Worker.mro())