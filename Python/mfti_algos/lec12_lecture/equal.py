# O(n)
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


def equal_pw(str1, str2):
    return True if str1 == str2 else False


def main():
    print(equal("Hello", "Hello"))
    print(equal("Hello1", "Hello2"))
    print(equal("Hello", "Helloo"))

    print(equal_pw("Hello", "Hello"))
    print(equal_pw("Hello1", "Hello2"))
    print(equal_pw("Hello", "Helloo"))


if __name__ == "__main__":
    main()
