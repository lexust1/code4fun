# Сдать решение задачи E-Скобочные выражения
# Скобочки
#
# Некоторые скобочные структуры правильные, другие — неправильные.
# Ваша задача — определить правильная ли скобочная структура.
#
# Входные данные
#
# Слово в алфавите из двух круглых скобочек ( и ). Длина слова
# меньше 4001
#
# Выходные данные
#
# Либо NO, либо YES
#
# Примеры
#
# Вход        Выход
#
# ()          YES
#
# )(          NO
#
# ()(())()    YES
#
def check_brackets(brackets: str) -> str:
    """
    Checks if the given string of brackets is balanced.

    Args:
        brackets (str): The string of brackets to check.

    Returns:
        str: "YES" if the brackets are balanced, "NO" otherwise.
    """
    stack = []
    for char in brackets:
        if char == "(":
            stack.append("(")
        else:  # char == ")"
            if not stack:
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"


def main():
    """The entry point."""
    brackets = input("Input brackets: ")
    print(check_brackets(brackets))


if __name__ == "__main__":
    main()
