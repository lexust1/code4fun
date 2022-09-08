# 70. The implementation of the classes: Product and Warehouse is given. 

# To the Product class, add a _str_( ) method that is an informal 
# representation of the Product class.

# An example of how the _str_( ) method works. 

# The code below:
# returns:
# product = Product(1 Laptop', 3900.0) 
# print(product)

# Then create an instance of the Product class named product with the arguments 
# passed:

#  • 'Mobile Phone', 1990.0

# In response, print the product instance to the console. Expected result:
# Product Name: Mobile Phone | Price: 1990.0

import uuid
    
class Product:
    
    def __init__(self, product_name, price):
        self.product_name  = product_name
        self.price = price
        self.product_id = self.get_id()
      
    def __repr__(self):
        return ("Product(product_name = {}, price = {})".
                format(self.product_name, self.price))  
    
    def __str__(self):
        return "Product Name: {} | Price: {}".format(self.product_name, 
                                                     self.price)

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
        

product = Product('Mobile Phone', 1990)
print(product)
print(str(product))
print(repr(product))

