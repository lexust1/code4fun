# Поиск элемента x в листе a:
n = int(input("Enter a number of elements in list: "))
a = [0] * n
for k in range(n):
    a[k] = int(input("Enter a value: "))
print(a)
x = int(input("Enter x: "))
for k in range(n):
    if a[k] == x:
        print(k)

        