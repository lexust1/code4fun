# 69. The implementation of the classes: Product and Warehouse is given. 

# To the Warehouse class, add a method named remove_product( ) that allows you 
# to remove an instance of the Product class from the products list with 
# a given product name. 

# If the product name is not in the products list, just skip.

# Next, create an instance of the Warehouse class named warehouse. 
# Using the add_product() method add the following products:
# 'Laptop', 3900.0 'Mobile Phone', 1990.0 • 'Camera', 2900.0

# Then, using the remove_product() method, remove the product named 
# 'Mobile Phone' . 

# In response, print the products attribute of the warehouse instance to the 
# console.
# Expected result:
# [Product(product_name='Laptop', price=3900.0), 
#  Product(product_name='Camera', price=2900.0)]

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
        
    def add_product(self, product_name, price):
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

            
    def remove_product(self, product_name):
        [self.products.remove(product) for product in self.products 
         if product.product_name == product_name]
        
warehouse = Warehouse()
print(warehouse.products)      

warehouse.add_product('Laptop', 3900)
print(warehouse.products) 
warehouse.add_product('Mobile Phone', 1990)
print(warehouse.products) 
warehouse.add_product('Camera', 2900)
print(warehouse.products)         
warehouse.remove_product('Mobile Phone')
print(warehouse.products)   