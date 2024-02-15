# Сдать решение задачи G-Период строки
#
# Дана непустая строка s. Нужно найти такое наибольшее число k, что s
# совпадает со строкой t, выписанной k раз подряд.
#
# Формат входных данных
# Одна строка длины N, 0 < N ≤ 10^6, состоящая только из маленьких
# латинских букв.
#
# Формат выходных данных
# Одно число - наибольшее возможное k.
#
# Примеры
# Ввод	Вывод
# aaaaa   5
#
#
# Ввод	        Вывод
# abcabcabc       3
#
#
# Ввод	Вывод
# abab    2
def compute_pi_function(string):
    """
    Вычисляет пи-функцию для заданной строки.
    Пи-функция указывает длину наибольшего совпадающего префикса,
    который также является суффиксом
    для подстроки, заканчивающейся на каждом символе.

    Args:
    string (str): Строка, для которой вычисляется пи-функция.

    Returns:
    list: Массив, представляющий пи-функцию строки.
    """
    length = len(string)
    pi = [0] * length  # Инициализация массива пи-функции нулями
    j = 0  # Индекс для отслеживания длины текущего префикса
    # Проходим по строке, начиная со второго символа
    for i in range(1, length):
        # Пока j > 0 и текущий символ не совпадает с символом в префиксе,
        # возвращаемся к предыдущему возможному префиксу
        while j > 0 and string[j] != string[i]:
            j = pi[j - 1]
        # Если символы совпадают, увеличиваем j и обновляем пи-функцию
        if string[j] == string[i]:
            j += 1
        pi[i] = j
    return pi


def find_max_repetitions(s):
    """
    Находит максимальное количество повторений минимального периода в
    строке.

    Args:
    s (str): Строка, для которой требуется найти максимальное количество
    повторений.

    Returns:
    int: Максимальное количество повторений минимального периода в
    строке.
    """
    n = len(s)  # Длина исходной строки
    pi = compute_pi_function(s)  # Вычисление префикс-функции для строки
    period_length = n - pi[-1]  # Определение длины периода
    # Проверка, делится ли длина строки на длину периода
    if period_length and n % period_length == 0:
        # Возвращение максимального количества повторений минимального
        # периода
        return n // period_length
    else:
        # Возвращение 1, если строка не имеет повторяющегося периода
        return 1


def main():
    s = "aaaaa"
    print(find_max_repetitions(s))
    s = "abcabcabc"
    print(find_max_repetitions(s))
    s = "abab"
    print(find_max_repetitions(s))


if __name__ == "__main__":
    main()