# Инверсия листа
n = int(input("Enter a number of elements in list: "))
a = [0] * n
for k in range(n):
    a[k] = int(input("Enter a value: "))
print(a)
for k in range(n // 2):
    a[k], a[n-k-1] = a[n-k-1], a[k]
print(a)