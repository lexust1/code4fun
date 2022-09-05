# 40. The following classes are defined. Add the _init_() method to the Person 
# class, which sets three attributes:
# • firstname
# • lastname
# • age

# Then create an instance of the Worker class passing the following arguments:
# • 'John'
# * 'Doe'
# • 35

# In response, print the value of the _dict_ attribute of this instance.

# Expected result:
# {‘first_name’ : 'John', 'last_name': 'Doe', 'age': 35}

class Person:
    
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class Department:
    pass

class Worker(Person, Department):
    pass

worker = Worker('John', 'Doe', 35)
print(worker.__dict__)