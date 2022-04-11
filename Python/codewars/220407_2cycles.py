# Your task, is to create NxN multiplication table, of size provided 
# in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

# 1
def multiplication_table(size):
    first_row = list(range(1, size + 1))
    table = []
    table.append(first_row)
    for count in range(2, size + 1):
        next_row = []
        for el1 in first_row:
            el2 = el1 * count
            next_row.append(el2)
        table.append(next_row)    
        count += 1
        
    return table

# 2
def multiplication_table(size):
    table = []
    for count, el in enumerate(range(1, size + 1), 1):
        row = []
        [row.append(el * count) for el in range(1, size + 1)]
        table.append(row)    
       
    return table

# 3
def multiplication_table(size):
       
    return [[el1 * el2 for el1 in range(1, size + 1)] for el2 in range(1, size + 1)]