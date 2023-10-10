# Сдать решение задачи B-Определение типа треугольника
#
# Определите тип треугольника (остроугольный, тупоугольный,
# прямоугольный) с данными сторонами.
#
# Формат входных данных
# Даны три натуральных числа – стороны треугольника. Каждое число
# вводится с новой строки.
#
# Формат выходных данных
# Необходимо вывести одно из слов: right для прямоугольного
# треугольника, acute для остроугольного треугольника, obtuse для
# тупоугольного треугольника или impossible, треугольника с такими
# сторонами не существует.
#
# Примеры
# Ввод	Вывод
# 3       right
# 4
# 5

def create_input_data() -> list:
    """Creates an array with triangle sides."""
    arr = []
    print(
        "Input the triangle sides.\nEvery side is a new line.\n"
        "Use Whitespace + Enter to quit."
    )
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(int(inp))
    return arr


def get_triangle_type(arr):
    """Checks the triangle type."""
    # Find the squares of the sides (ss).
    # The longest and short sides (lls).
    ls = max(arr)
    # Find the squares of other sides (ss1 and ss2).
    arr.remove(ls)
    s1 = arr[0]
    s2 = arr[1]
    if s1 + s2 < ls:
        return "impossible"
    elif s1 ** 2 + s2 ** 2 == ls ** 2:
        return "right"
    elif s1 ** 2 + s2 ** 2 > ls ** 2:
        return "acute"
    else:
        return "obtuse"

        
def main():
    return get_triangle_type(create_input_data())


if __name__ == "__main__":
    main()
