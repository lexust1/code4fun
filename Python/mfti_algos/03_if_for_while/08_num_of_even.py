# Посчитать количество четных элементов в массиве целых чисел,
# заканчивающихся нулём. Сам ноль учитывать не надо.
#
# Формат входных данных
# Массив чисел, заканчивающийся нулём (каждое число с новой строки,
# ноль не входит в массив)
#
# Формат выходных данных
# Одно число — результат.
#
# Примеры
# Ввод	  Вывод
# 1 2 0   1
#
#
# Ввод	  Вывод
# 1 -1 0  0
sequence = []
while True:
    user_input = int(input("Enter a value (or 0 to stop): "))
    if user_input == 0:
        break
    sequence.append(user_input)
print(sequence)

cnt_even = 0
for el in sequence:
    if el % 2 == 0:
        cnt_even += 1
print(f"A number of evens: {cnt_even}")
