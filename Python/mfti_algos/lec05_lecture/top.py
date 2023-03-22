# Заполненность.
a = [0] * 1000
top = 0
while True:
    user_input = int(input("Enter an integer (or zero to stop): "))
    if user_input == 0:
        break
    a[top] = user_input
    top += 1
print(a[0:top])
for k in range(top - 1, -1, -1):
    print(a[k])

