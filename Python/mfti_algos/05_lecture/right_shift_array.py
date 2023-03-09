# Сдвиг листа вправо.
n = int(input("Enter a number of elements in list: "))
a = [0] * n
for k in range(n):
    a[k] = int(input("Enter a value: "))
print(a)

tmp = a[n - 1]
for k in range(n - 1, -1, -1):
    a[k] = a[k-1]
a[0] = tmp
print(a)