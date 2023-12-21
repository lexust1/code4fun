# Упражнение №5: Префикс-функция
# Напишите префикс-функцию. Пусть заголовком ее будет def p_func(s, n):
#
# O(m + n)
# Алгоритм Кнута-Морриса-Пратта (КМП) — это эффективный метод поиска
# подстроки, который использует пи-функцию для ускорения процесса путем
# избегания повторного сравнения символов.
#
# Префикс
# Префикс строки — это любой начальный сегмент этой строки. Другими
# словами, если у вас есть строка, префиксом будет любая часть этой
# строки, которая начинается с первого символа и заканчивается на любом
# другом символе внутри строки. Префикс может быть коротким, длинным или
# даже пустым (если не включает ни одного символа).
#
# Суффикс
# Суффикс строки — это любой конечный сегмент этой строки. Это значит,
# что суффиксом будет любая часть строки, начинающаяся с одного из её
# символов и продолжающаяся до конца строки. Как и префикс, суффикс
# может быть любой длины, включая пустую строку.
#
# Пример
# Рассмотрим строку "абракадабра". Вот несколько примеров префиксов и
# суффиксов для этой строки:
#
# Префиксы: "а", "абр", "абракад", "абракадабра" (вся строка), и
# "" (пустая строка).
# Суффиксы: "а", "дабра", "акадабра", "абракадабра" (вся строка), и
# "" (пустая строка).
# В контексте алгоритма Кнута-Морриса-Пратта, пи-функция помогает
# определять, насколько можно сдвинуть поиск подстроки вперёд, сравнивая
# префиксы и суффиксы подстроки для нахождения максимально возможного
# совпадения. Это позволяет избежать повторного сравнения символов,
# которые уже были сравнены.

# Разберем вычисление пи-функции для подстроки "ABCDABD", чтобы увидеть,
# как она работает на каждом шаге:
#
# Индекс 0 (символ 'A'):
#
# Подстрока: "A"
# Совпадающих префиксов и суффиксов нет.
# Пи-функция: 0
# Индекс 1 (символ 'B'):
#
# Подстрока: "AB"
# Префикс "A" не совпадает с суффиксом "B".
# Пи-функция: 0
# Индекс 2 (символ 'C'):
#
# Подстрока: "ABC"
# Нет совпадающих префиксов и суффиксов.
# Пи-функция: 0
# Индекс 3 (символ 'D'):
#
# Подстрока: "ABCD"
# Опять нет совпадающих префиксов и суффиксов.
# Пи-функция: 0
# Индекс 4 (второй символ 'A'):
#
# Подстрока: "ABCDA"
# Единственный совпадающий префикс и суффикс – "A".
# Пи-функция: 1
# Индекс 5 (второй символ 'B'):
#
# Подстрока: "ABCDAB"
# Совпадают префикс "AB" и суффикс "AB".
# Пи-функция: 2
# Индекс 6 (символ 'D'):
#
# Подстрока: "ABCDABD"
# Нет совпадающих префиксов и суффиксов.
# Пи-функция: 0
# В результате мы получаем массив пи-функции для "ABCDABD" следующего
# вида:
#
# A B C D A B D
# 0 0 0 0 1 2 0
#
# Как видите, на каждом шаге мы анализируем подстроку, заканчивающуюся
# на текущем символе, и ищем наибольшее совпадение префикса и суффикса.
# Эти значения пи-функции затем используются в алгоритме КМП для
# определения, насколько можно сдвинуть подстроку в случае несовпадения
# символов в основной строке, что позволяет избежать повторного
# сравнения символов, уже проверенных ранее.
def p_function(string, n):
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


def main():
    s = "abcxabcdabcdabcy"
    print(p_function(s, len(s)))


if __name__ == "__main__":
    main()
