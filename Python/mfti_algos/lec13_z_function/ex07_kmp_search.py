# Упражнение №7: Поиск подстроки онлайн
# В первой строке ввода - число n
# , количество букв в паттерне. Во второй строке - паттерн, строка
# которую нужно искать в тексте. В каждой из последующих строк - символы
# текста, по одному в каждой строке. Необходимо вывести позиции
# вхождений паттерна в текст. Длина текста заранее не известна, он может
# быть очень большим.

# См. ex06_kmp_search.py. Смысл один в один, только входные данные
# слегка другие.
# Данный алгоритм хорош тем, что если мы не меняем подстроку (по сути,
# ищем тоже самое слово каждый раз) пи-функция не требует повторного
# использования. Выходной результат пи-функции, примененной к строке,
# остается прежним. Только алгоритм КМП будет использоваться повторно,
# но он может продолжить с того места, где мы остановились. Ему нет
# необходимости заглядывать назад, все необходимые сдвиги он берет
# из пи-функции, которая остается неизменной.
#
# С z-функций такой трюк повторить сложнее, т.к. при появлении новых
# символов алгоритм может заглядывать и назад, т.е. часть предыдущих
# расчетов надо переделать.
#
# Таким образом, при появлении новых символов в строке, мы просто заново
# применяем KMP_search к новому тексту. Результат пи-функции,
# примененной к подстроке, остается прежним. При этом пи-функцию внутри
# KMP_search надо исключить, чтобы не повторять расчет каждый раз.
#
def create_input_data():
    print("Input the data: ")
    arr = []
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    return arr


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


def KMP_search(main_string, substring, pi):
    """
    Выполняет поиск подстроки в строке, используя алгоритм
    Кнута-Морриса-Пратта.
    Алгоритм использует пи-функцию для определения, насколько сдвигать
    поиск, тем самым уменьшая количество необходимых сравнений.

    Args:
    main_string (str): Основная строка для поиска.
    substring (str): Подстрока, которую нужно найти.
    pi (list): пи-функция

    Returns:
    int: Индекс начала подстроки в основной строке или -1, если
    подстрока не найдена.
    """
    # pi = compute_pi_function(substring)  # Вычисление пи-функции для подстроки  закоментировано, чтобы не повторять каждый раз
    j = 0  # Индекс в подстроке
    # Проходим по основной строке
    for i in range(len(main_string)):
        # Пока j > 0 и символы не совпадают, используем пи-функцию для сдвига
        while j > 0 and main_string[i] != substring[j]:
            j = pi[j - 1]
        # Если символы совпадают, увеличиваем j
        if main_string[i] == substring[j]:
            j += 1
        # Если достигнут конец подстроки, нашли совпадение
        if j == len(substring):
            return i - j + 1  # Возвращаем индекс начала подстроки в основной строке
    return -1  # Если подстрока не найдена


def main():
    arr = create_input_data()
    substring = arr[1]
    main_string = ""
    pi = compute_pi_function(substring)
    i = 0
    while i < len(arr[2 : ]):
        main_string += arr[2 + i]
        pos = KMP_search(main_string, substring, pi)
        i += 1
        # print(i, pos)
        print(f"i = {i - 1}, main_string = {main_string}, substring = {substring}, position = {pos}")


if __name__ == "__main__":
    main()


