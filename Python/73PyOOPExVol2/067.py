# 67. An implementation of the Product class is given. 

# Implement a class named Warehouse which in the init ( ) method sets 
# an instance attribute of the Warehouse class named products to
# an empty list.

# Then create an instance of the Warehouse class named warehouse and display 
# the value of the products attribute to the console.

# Expected result:
# []

import uuid
    
class Product:
    
    def __init__(self, product_name, price):
        self.product_name  = product_name
        self.price = price
        self.product_id = self.get_id()
      
    def __repr__(self):
        return ("Product(product_name = {}, price = {})".
                format(self.product_name, self.price))    

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    
class Warehouse:
    
    def __init__(self):
        self.products = []
        
warehouse = Warehouse()
print(warehouse.products)        
