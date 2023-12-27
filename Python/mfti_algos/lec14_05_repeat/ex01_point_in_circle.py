# Сдать решение задачи A-Принадлежность точки кругу
#
# Даны координаты точки и радиус круга с центром в начале координат.
# Определить, принадлежит ли данная точка кругу. Напомним, что круг –
# это часть плоскости, состоящая из всех точек окружности и всех точек,
# лежащих внутри окружности.
#
# Формат входных данных
# Три целых числа на одной строке: координата точки по оси x,
# координата точки по оси y, радиус круга r (r > 0).
#
# Формат выходных данных
# Вывести "YES" без кавычек, если точка принадлежит кругу, "NO" без
# кавычек в противном случае.
#
# Примеры
# Ввод	Вывод
# 0 0 1   YES
#
# Ввод	Вывод
# -1 3 1  NO
#
# Оставляем тот же подход, что было в lec06_arrays.
def create_input_data():
    inp_str = input("Input 3 integer with whitespaces (0 0 1) in one line: ")
    input_data = [int(el) for el in inp_str.split()]
    return input_data


def compare_radius_and_point(input_data):
    x = input_data[0]
    y = input_data[1]
    r = input_data[2]
    if x ** 2 + y ** 2 <= r ** 2:
        return "Yes"
    else:
        return "No"


def main():
    lst = create_input_data()
    res = compare_radius_and_point(lst)
    print(res)


if __name__ == "__main__":
    main()
