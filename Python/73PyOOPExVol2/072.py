# 72. The implementation of the classes: Product and Warehouse is given. 

# Add a method called sort_by_price( ) to the Warehouse class that returns 
# an alphabetically sorted list of products. 

# The sort_by_price( ) method also takes an argument ascending set to True 
# by default, which means an ascending sort. 

# If False is passed, reverse the sort order.

# Then create an instance of the Warehouse class named warehouse and execute 
# the following code:
# warehouse.add_product('Laptop', 3900.0) 
# warehouse.add_product('Mobile Phone', 1990.0)
# warehouse.add_product('Camera', 2900.0) 
# warehouse.add_product('USB Cable', 24.9) 
# warehouse.add_product('House', 49.0)

# In response, use the sort_by_price( ) method to print a sorted list of 
# products to the console as shown below.

# Expected result:
    
# Product(product_name='USB Cable', price=24.9)
# Product(product_name='Mouse', price=49.0) 
# Product(product_name='Mobile Phone', price=1990.0) 
# Product(product_name='Camera', price=2900.O) 
# Product(product_name='Laptop', price=3900.0)

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
        
    def sort_by_price(self, ascending=True):
        return sorted(self.products, 
                      key=lambda product: product.price, 
                      reverse=not ascending)

warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0) 
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0) 
warehouse.add_product('USB Cable', 24.9) 
warehouse.add_product('House', 49.0)
print(warehouse.display_products())

[print(product) for product in warehouse.sort_by_price()]