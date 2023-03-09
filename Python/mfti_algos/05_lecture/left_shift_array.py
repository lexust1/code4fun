# Сдвиг листа влево
n = int(input("Enter a number of elements in list: "))
a = [0] * n
for k in range(n):
    a[k] = int(input("Enter a value: "))
print(a)


tmp = a[0]
for k in range(n - 1):
    a[k] = a[k+1]
a[n - 1] = tmp
print(a)

