# Сдать решение задачи I-B-функция
#
# Зафиксируем строку L. Будем называть её подстроку K особенной, если у
# неё есть как минимум три различных вхождения в L, среди которых
# префикс и суффикс строки L.
#
# Пусть теперь дана строка S, состоящая из N символов. Пусть B(i) -
# длина максимальной особенной подстроки у строки, образованной
# первыми i символами S.
#
# Напишите программу, которая вычислит значения функции B для заданной
# строчки для всех возможных значений i от 1 до N (нумерация от 1).
#
# Формат входных данных
# В единственной строке записана строка, состоящая только из больших
# и/или маленьких латинских букв. Длина строки 1 <= N <= 200000.
#
# Формат выходных данных
# В выходной файл выведите N чисел — значения функции B(1), B(2), … B(N).
#
# Примеры
# Ввод	        Вывод
# aaaaa           0 0 1 2 3

# Не факт, что получившийся алгоритм идеален. Полагаю, можно было залезть
# во внутрь z-функции или пи-функции и сделать даже более хитрый алгоритм,
# чтобы использовать часть расчитанных ранее значение, когда мы делаем перебор
# в строке. Но решил ограничиться O(n^2) с учетом дефицита времени.
# На первый взгляд может показать, что асимпотика по времени у этого алгоритма
# O(n^3). Но надо внимательно смотреть на функции calculate_unique_substring(s),
# где большинство строк будут исключать через допусловиями. Т.е. по факту ближе
# к O(n^2) чем O(n^3).
#


def z_func(s, n):
    """
    Вычисляет Z-функцию для строки.

    Args:
    s (str): Строка, для которой вычисляется Z-функция.

    Returns:
    list: Список, содержащий значения Z-функции для каждого индекса строки.
    """
    n = len(s)  # Определяем длину строки s
    z = [0] * n  # Создаем массив Z-функции длины n, инициализированный нулями
    l, r = 0, 0  # Устанавливаем начальные границы самого правого отрезка совпадения
    for i in range(1, n):  # Итерируемся по всем позициям строки, начиная со второй
        if i <= r:  # Проверяем, находится ли текущая позиция i в пределах отрезка [l; r]
            # Инициализируем z[i] меньшим из двух значений:
            # 1. r - i + 1: Максимальное количество символов, которое может совпадать с началом строки,
            #    начиная с позиции i, на основе уже известных данных.
            # 2. z[i - l]: Соответствующее значение Z-функции из предыдущего совпадения.
            # Это предотвращает необходимость в повторных сравнениях символов.
            z[i] = min(r - i + 1, z[i - l])
        # Продолжаем сравнивать символы после предполагаемого совпадения до тех пор,
        # пока они совпадают и пока не достигнут конца строки
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:  # Если новый отрезок совпадения выходит за границу r
            l, r = i, i + z[i] - 1  # Обновляем границы самого правого отрезка совпадения
    return z


def find_occurrences(s1, s2):
    """
    Находит все вхождения строки s2 в строке s1.

    Args:
    s1 (str): Строка, в которой ищутся вхождения.
    s2 (str): Подстрока, вхождения которой ищутся в s1.

    Returns:
    list: Список индексов, на которых начинаются вхождения s2 в s1.
    """
    concatenated = s2 + "#" + s1  # Объединяем строки с уникальным разделителем
    z = z_func(concatenated, len(concatenated))  # Вычисляем Z-функцию для объединенной строки
    len_s2 = len(s2)  # Длина искомой подстроки s2
    occurrences = []  # Список для хранения индексов вхождений

    # Проходим по Z-функции, начиная с индекса, следующего за s2 и разделителем
    for i in range(len_s2 + 1, len(concatenated)):
        # Проверяем, совпадает ли значение Z-функции с длиной s2
        # и соответствует ли найденная подстрока s2
        if z[i] == len_s2 and concatenated[i : i + z[i]] == s2:
            # Добавляем индекс начала вхождения в s1
            occurrences.append(i - (len_s2 + 1))
    return occurrences


def calculate_unique_substring(s):
    """
    Вычисляет длину максимальной особенной подстроки в данной строке.

    Особенная подстрока определяется как подстрока, которая одновременно является
    префиксом и суффиксом данной строки и встречается в ней как минимум три раза.

    Args:
    s (str): Строка для поиска особенной подстроки.

    Returns:
    int: Длина максимальной особенной подстроки. Возвращает 0, если таковая не найдена.
    """
    if len(s) < 3:
        # Если длина строки меньше трех, особенной подстроки не существует
        return 0
    end = len(s)
    # Список для хранения длин всех найденных особенных подстрок
    lengths = []
    # Итерируемся по всем возможным длинам подстрок
    for i in range(1, end + 1 - 2):
        prefix = s[:i]  # Выделяем префикс текущей длины
        suffix = s[-i:]  # Выделяем суффикс текущей длины
        # Проверяем, является ли подстрока одновременно префиксом и суффиксом
        # и что длина префикса не равна длине строки (тогда 3 включение не войдет)
        if prefix == suffix and len(prefix) != len(s):
            # Находим все вхождения подстроки в строку
            occurrences = find_occurrences(s, prefix)
            # Проверяем условие наличия минимум трех вхождений
            if len(occurrences) >= 3:
                # Добавляем длину подстроки в список
                lengths.append(len(prefix))
    # Возвращаем максимальную длину из найденных подстрок или 0, если таковых нет
    return max(lengths) if lengths else 0


def b_func(s, n):
    """
    Вычисляет значения функции B для каждого префикса заданной строки
    через ограничение длины при помощи n.

    Функция B(i) определяется как длина максимальной особенной подстроки
    строки, составленной из первых i символов исходной строки.

    Args:
    s (str): Строка, для которой вычисляется функция B.
    n (int): Максимальная длина подстроки.

    Returns:
    list: Список значений функции B для каждого префикса строки.
    """
    # Список для хранения значений функции B
    arr = []
    # Итерируемся по всем префиксам строки s
    for i in range(1, n + 1):
        # Получаем префикс строки длиной i
        substring = s[:i]
        # Вычисляем значение функции B для данного префикса
        arr.append(calculate_unique_substring(substring))
    return arr  # Возвращаем список значений функции B


def main():
    print(b_func("aaaaaaa", 5))
    print(b_func("abcabcabc", 9))
    # print("a:", calculate_unique_substring("a"))
    # print("aa:", calculate_unique_substring("aa"))
    # print("aaa:", calculate_unique_substring("aaa"))
    # print("aaaa:", calculate_unique_substring("aaaa"))
    # print("aaaaa:", calculate_unique_substring("aaaaa"))
    # print("abcabcabc:", calculate_unique_substring("abcabcabc"))
    # print("abc:", calculate_unique_substring("abc"))
    # print("aaaaaa:", calculate_unique_substring("aaaaaa"))
    # print("aaaaaaa:", calculate_unique_substring("aaaaaaa"))
    # print(calculate_unique_substring("abcdxabcdyabcd"))
    # print(calculate_unique_substring("aaaa"))
    # calculate_unique_substring("abcxabcyabcz")
    # calculate_unique_substring("abcxabcyabczz")

    # print(calculate_B_function("aaaaa"))
    # print(z_func("abababa"))
    # print(z_func("abcababc"))
    # print(z_func("abcabcabc"))


if __name__ == "__main__":
    main()
