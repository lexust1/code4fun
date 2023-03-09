# Решето Эратосфена
n = int(input("Enter a number of elements in list: "))
a = [True] * n
a[0] = a[1] = False


for k in range(2, int(n ** 0.5) + 1):
    if a[k]:
        for m in range(2 * k, n, k):
            a[m] = False
for k in range(n):
    print(k, "-", "primary" if a[k] else "not primary")