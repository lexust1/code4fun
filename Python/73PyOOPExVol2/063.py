# 63. The Client class is implemented. 

# The following four instances of the Client class:

# For example, the following code:

#  Clientl = Client(‘Tom’, ‘sample@gmail.com’)
#  client2 = Client(‘Donald', ‘sales@yahoo.com’) 
#  client3 = Client('Mike’, ‘sales-contact@yahoo.com’) 
#  client4 = Client(1 Lisa1, 'info@gmail.com' )

# Search for all customers with the word ‘sales ' email address. 
# In response, print the names of the customers as a list to the console.

# Expected result: ['Donald', 'Mike']

class ClientList(list):
    def search_email(self, value):
        return [client for client in self if value in client.email]

class Client:
    
    all_clients = ClientList()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)
        
    def __repr__(self):
        return "Client(name={}, email={})".format(self.name, self.email)
    
client1 = Client('Tom', 'sample@gmail.com') 
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')  
client4 = Client('Lisa', 'info@gmail.com')


[print(cl.name) for cl in Client.all_clients.search_email('sales')]
