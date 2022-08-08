# 27. The following Doc class is implemented for storing text documents.

# Implement the _iadd_() special method to perform extended assignments. 
# Concatenate two instances with the string ‘ & ‘
# Example:
# [IN]: doc1 = Doc('Finance')
# [IN]: doc2 = Doc('Accounting')
# [IN]: doc1 += doc2 
# [IN]: print(doc1)
# [OUT]: Finance & Accounting

# Then create two instances of the Doc class for the following documents:
# • 'sport'
# • 'activity'
# and assign according to the variables:
# • doc1
# * doc2

# Perform extended assignment 
# • docl + = doc2
# Print docl instance to the console.

# Expected result: sport & activity

class Doc:
    
    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return "Doc{}".format(self.string)

    def __str__(self):
        return "{}".format(self.string)

    # def __add__(self, other):
    #     return Doc(self.string + other.string)

    # def __lt__(self, other):
    #     return len(self.string) < len(other.string)

    def __iadd__(self, other):
        return Doc(self.string + ' & ' + other.string)
    
doc1 = Doc('sport')
doc2 = Doc('activity')

doc1 += doc2

print(doc1)    