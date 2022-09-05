# 49. An implementation of the Taxpayer abstract class is given. 

# Create a class derived from the TaxPayer class named WorkerTaxPayer 
# that implements the caicuiate_tax( ) method that calculates the tax value
#  according to the rule:
# • up to the amount of 80,000 -> 17% tax rate
# • everything above 80,000 -> 32% tax rate

# Then create two instances of WorkerTaxPayer named workerl and worker2 and 
# salaries of 70,000 and 95,000 respectively. 

# In response, by calling caicuiate_tax() print the calculated tax for both 
# instances to the console.

# Expected result: 
# 11900.0
# 18400.0

from abc import ABC, abstractmethod

class TaxPayer(ABC):
    
    def __init__(self, salary):
        self.salary = salary
        
    @abstractmethod
    def calculate_tax(self):
        pass

class StudentTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.15

class DisabledTaxPayer(TaxPayer):

    def calculate_tax(self):
        return min(self.salary * 0.15, 5000)

class WorkerTaxPayer(TaxPayer):
    
    def calculate_tax(self):
        if self.salary <= 80000:
            return 0.17 * self.salary
        else:
            return 0.17 * 80000 + (self.salary - 80000) * 0.32 
        
        
workertaxpayer1 = WorkerTaxPayer(70000)
print(workertaxpayer1.calculate_tax())

workertaxpayer1 = WorkerTaxPayer(95000)
print(workertaxpayer1.calculate_tax())