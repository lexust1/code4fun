
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
    
def factorial_recursive(n):
    while n != 1:
        return n*factorial_recursive(n-1)
    return n    
    
factorial_recursive(3)    