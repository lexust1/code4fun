# Копирование из одного листа в другой.
n = int(input("Enter a number of elements in list: "))
a = [0] * n
b = [0] * n
for k in range(n):
    a[k] = int(input("Enter a value: "))
print(a)
for k in range(n):
    b[k] = a[k]
print(b)
