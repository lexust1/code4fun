# 71. The implementation of the classes: Product and Warehouse is given. 

# Add a method to the Warehouse class named dispiay_products() that displays 
# all products in the products attribute of the Warehouse class.

# Then create an instance of the Warehouse class named warehouse and execute 
# the following code:
    
# warehouse.add_product('Laptop', 3900.0) 
# warehouse.add_product('Mobile Phone', 1990.0) 
# warehouse.add_product('Camera', 2900.0)

# In response, call dispiay_products() method on the warehouse instance.

# Expected result:
#     Product Name: Laptop | Price: 3900.0 
#     Product Name: Mobile Phone | Price: 1990.0 
#     Product Name: Camera | Price: 2900.0
    

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
        
    def display_products(self):
        [print(product) for product in self.products]

warehouse = Warehouse()

warehouse.add_product('Laptop', 3900)
warehouse.add_product('Mobile Phone', 1990)
warehouse.add_product('Camera', 2900)
        

print(warehouse.display_products())    

    