# 46. Create an abstract class named Taxpayer. 

# In the _init_() method set an instance attribute
# (without validation) called salary. 

# Then add an abstract method called calculate_tax() 
# (use the @abstractmethod decorator).

from abc import ABC, abstractmethod

class Taxpayer(ABC):
    
    def __init__(self, salary):
        self.salary = salary
        
    @abstractmethod
    def calculate_tax(self):
        pass
        