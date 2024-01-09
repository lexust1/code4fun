# Упражнение №9: Период строки
# Для данной строки s найти строку p минимальной длины, такую что s
#  можно предстваить как конкатенацию одной или нескольких копий p.
# Используйте префикс-функцию.

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


def find_period(s):
    """
    Находит минимальный период строки.

    Args:
    s (str): Строка, для которой требуется найти минимальный период.

    Returns:
    tuple: Кортеж, содержащий строку, являющуюся минимальным периодом, и её длину.
           Если строка не может быть представлена как конкатенация копий некоторой подстроки,
           возвращает исходную строку и её длину.

    Описание работы функции:
    1. Вычисление префикс-функции для заданной строки.
    2. Определение длины периода как разность между длиной строки и последним значением префикс-функции.
    3. Проверка, делится ли длина строки на длину предполагаемого периода без остатка.
       Если делится, возвращается подстрока, являющаяся периодом, и её длина.
       В противном случае, возвращается исходная строка и её длина.
    """
    n = len(s)  # Длина исходной строки
    pi = compute_pi_function(s)  # Вычисление префикс-функции для строки
    period_length = n - pi[-1]  # Определение длины периода
    # Проверка, делится ли длина строки на длину периода
    if n % period_length == 0:
        # Возвращение подстроки, являющейся периодом, и её длины
        return s[:period_length], len(s[:period_length])
    else:
        # Возвращение исходной строки и её длины, если период не найден
        return s, len(s)


def main():
    s = "abcabcabc"
    print(find_period(s))


if __name__ == "__main__":
    main()