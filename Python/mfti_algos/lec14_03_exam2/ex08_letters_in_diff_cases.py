# Сдать решение задачи H-Количество букв разного регистра
#
# Посчитать количество строчных (маленьких) и прописных (больших) букв
# в введенной строке. Важная подсказка:
# в питоне есть функция ord(chr) -> int.
# Возвращает числовое представление для указанного символа.
# Например, ord('a') вернет 97. Коды идут последовательно,
# то есть ord('a') = 97, ord('b') = 98 и так далее.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Два числа - количество прописных и строчных букв. Вывести в одну
# строку через пробел.
#
# Примеры
# Ввод	        Вывод
# AAAaa BBb       5 3
def count_lowercase_and_uppercase_letters(chars):
    """
    Подсчитывает количество строчных и прописных букв в строке.

    Args:
    - chars (str): Строка, в которой необходимо подсчитать буквы.

    Returns:
    tuple: Возвращает кортеж из двух элементов, первый элемент - количество прописных букв,
           второй элемент - количество строчных букв.
    """
    # Инициализация счетчиков для строчных и прописных букв
    cnt_lower = 0
    cnt_upper = 0
    # Перебор всех символов в строке
    for char in chars:
        # Если символ является строчной буквой (используется код ASCII символа)
        if 97 <= ord(char) <= 122:
            cnt_lower += 1  # Увеличиваем счетчик строчных букв
        # Если символ является прописной буквой (используется код ASCII символа)
        elif 65 <= ord(char) <= 90:
            cnt_upper += 1  # Увеличиваем счетчик прописных букв
    # Возвращаем результаты подсчета
    return cnt_upper, cnt_lower


def main():
    cnt_upper, cnt_lower = count_lowercase_and_uppercase_letters("AAAaa BBb")
    print(f"{cnt_upper} {cnt_lower}")


if __name__ == "__main__":
    main()