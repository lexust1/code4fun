# The Client class is implemented. 

# Create the following four instances of the Client class:

# For example, the following code:

#     Clientl = Client(‘Tom’, ‘sample@gmail.com’) 
#     client2 = Client(‘Donald', ‘sales@yahoo.com’) 
#     client3 = Client('Mike’, ‘sales-contact@yahoo.com’) 
#     client4 = Client(1 Lisa1, 'info@gmail.com' )

# Then search for all customers who have a gmail account 
# ( ‘gmail ' in email address). 
 
# In response, print result to the console as shown below.

# Expected result:
# Client(name='Tom', email='sample@gmail.com')
# Client(name='Donald', email='sales@gmail.com') 
# Client(name='Lisa', email='info@gmail.com')

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

print(Client.all_clients.search_email('gmail'))