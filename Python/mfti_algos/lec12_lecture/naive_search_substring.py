# O(n x m)
def equal(str1, str2):
    """
    Проверяет равенство двух строк.

    Args:
    str1 (str): Первая строка для сравнения.
    str2 (str): Вторая строка для сравнения.

    Returns:
    bool: True, если строки идентичны, и False в противном случае.
    """
    # Проверка длины строк
    if len(str1) != len(str2):
        return False
    # Поэлементное сравнение
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def naive_substring_search(main_string, substring):
    """
    Выполняет наивный поиск подстроки в строке. По сути, двигает окно.

    Args:
    main_string (str): Основная строка для поиска.
    substring (str): Подстрока, которую нужно найти.

    Returns:
    int: Индекс начала подстроки в основной строке или -1, если
        подстрока не найдена.
    """
    n = len(main_string)
    m = len(substring)
    # Перебираем все возможные начальные позиции подстроки в строке
    for i in range(n - m + 1):
        # Используем функцию equal для сравнения подстроки с частью основной строки
        if equal(main_string[i : i + m], substring):
            return i  # Возвращаем индекс, если подстрока найдена
    return -1  # Возвращаем -1, если подстрока не найдена


def main():
    print(naive_substring_search("Hello, world!", "world"))


if __name__ == "__main__":
    main()

