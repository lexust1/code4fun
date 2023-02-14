# Определите сумму всех элементов последовательности, завершающейся
# числом 0.
#
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
# Вводятся элементы последовательности по одному целому числу на строку.
# Числа вводятся, пока не будет введен 0.
#
# Формат выходных данных
# Вывести одно целое число - сумму последовательности.
#
# Примеры
# Ввод	Вывод
# 5       15
# 3
# 10
# 0
#
#
# Ввод	Вывод
# 17      13
# -4
# 0
sequence = []
while True:
    user_input = int(input("Enter a value (or use 0 to finish): "))
    if user_input == 0:
        break
    sequence.append(user_input)
print(sequence)

sum_of_sequence = 0
for el in sequence:
    sum_of_sequence += el
print(f"Sum of sequence: {sum_of_sequence}")

# OR
sum_of_sequence2 = sum(sequence)
print(f"Sum of sequence (2nd method): {sum_of_sequence2}")



