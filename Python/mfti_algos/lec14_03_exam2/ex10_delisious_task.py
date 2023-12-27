# Сдать решение задачи J-Самая вкусная задача
#
# Перевести число, записанное римскими цифрами, в число, записанное
# арабскими цифрами.
#
# Символы: I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000
#
# Выжимка из википедии:
#
# Натуральные числа записываются при помощи повторения этих цифр.
# При этом, если большая цифра стоит перед меньшей, то они складываются
# (принцип сложения), если же меньшая стоит перед большей, то меньшая
# вычитается из большей (принцип вычитания). Последнее правило
# применяется только во избежание четырёхкратного повторения одной и
# той же цифры.
#
# Формат входных данных
# Строка, представляющая число из римских цифр.
#
# Формат выходных данных
# Это же число в арабских цифрах. Стоит выводить число,
# конвертированное в строку, т.е. str(answer)
#
# Примеры
# Ввод	Вывод
# I       1
#
# Ввод	Вывод
# IV      4
def roman_to_arabic(roman):
    """
    Конвертирует число, записанное римскими цифрами, в число, записанное арабскими цифрами.

    Args:
    roman (str): Строка, представляющая число римскими цифрами.

    Returns:
    str: Строка, представляющая это же число арабскими цифрами.
    """
    # Словарь для конвертации римских цифр в арабские
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0  # Начальное значение арабского числа
    prev_value = 0  # Значение предыдущей цифры

    # Перебираем символы в строке справа налево
    for numeral in reversed(roman):
        value = roman_numerals[numeral]  # Получаем арабское значение для римской цифры
        # Если текущее значение меньше предыдущего, вычитаем его, иначе прибавляем
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value  # Обновляем предыдущее значение

    return str(arabic)


def roman_to_arabic2(roman):
    """
    Конвертирует число, записанное римскими цифрами, в число, записанное арабскими цифрами.

    Args:
    roman (str): Строка, представляющая число римскими цифрами.

    Returns:
    str: Строка, представляющая это же число арабскими цифрами.
    """
    # Списки для конвертации римских цифр в арабские (не используем словарь осознанно
    roman_numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabic_values = [1000, 500, 100, 50, 10, 5, 1]
    # Начальное значение арабского числа
    arabic = 0
    # Значение предыдущей цифры
    prev_value = 0
    # Перебираем символы в строке справа налево
    for numeral in reversed(roman):
        # Получаем арабское значение для римской цифры
        value = arabic_values[roman_numerals.index(numeral)]
        # Если текущее значение меньше предыдущего, вычитаем его, иначе прибавляем
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value  # Обновляем предыдущее значение
    return str(arabic)


def main():
    print("I", roman_to_arabic("I"))
    print("IV", roman_to_arabic("IV"))
    print("XXIV", roman_to_arabic("XXIV"))
    print("XXVIII", roman_to_arabic("XXVIII"))
    print("MDCLXXIV", roman_to_arabic("MDCLXXIV"))


if __name__ == "__main__":
    main()
