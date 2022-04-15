# You are given a secret message you need to decipher. Here are the things 
# you need to know to decipher it:

# For each word:

# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces

# Examples

# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'

import re

def decipher_this(string):
    list_of_words = [] 
    for word in string.split():
        # 1. The word does not have digits
        if word.isalpha() is False: 
            word = re.sub("^\d+", chr(int(re.search("^\d+", word).group())), 
                          word)          
        # 2. The word has less than 3 letters 
        if len(word) <= 2:
            list_of_words.append(word)   
        # 3. The word has 3 letters    
        elif len(word) == 3:
            new_word = word[0] + word[-1] + word[1]
            list_of_words.append(new_word)  
        # 4. The word has more than 3 letters    
        else:    
            new_word = word[0] + word[-1] + word [2:-1] + word[1]
            list_of_words.append(new_word)                    
    return ' '.join(list_of_words)
