# Дано трехзначное число. Найдите сумму его цифр.
#
# Формат входных данных
# Вводится трехзначное число.
#
# Формат выходных данных
# Одно число — сумма цифр.
#
# Примеры
# Ввод	Вывод
# 179   17

number = input("Input three-digit number: ")
sum_of_digits = 0
if len(number) == 3:
    for digit in number:
        sum_of_digits += int(digit)
    print(f"Sum of digits: {sum_of_digits}")
else:
    print("Your number is not three_digit number.")

