# Сдать решение задачи E-Результаты работы студентов в семестре
#
# Есть результаты работы студентов в семестре. Студентов выводить в
# порядке суммы их баллов. Требутеся вывести отсортированные результаты
# работ для каждого студента.
#
# Данные вводятся как: student_id value
#
# student_id принимает значения от 0 до N. value от 1 до 10
#
# Пример входных данных: 0 3 0 5 1 3 1 2
#
# Тут представленны данные о двух студента: 0 и 1. Сумма балов
# студента 0 - 8. Студента 1 - 5. Значит, сначала должны быть
# напечатаны результаты 0 студента, затем 1. Таким образом сначала
# надо вывести отсортированные результаты студента 0, затем студента 1:
#
# 5 3 3 2
#
# Напомним, что у list в питоне есть встроенный метод sort и есть
# функция sorted. У них есть параметр key, который определяет по каким
# значениям будет сортироваться объект. Например код ниже будет
# сортировать лист по длинне его элементов. Так же есть параметр
# reverse.
#
# a = ['###', '@', '??']
# a.sort(key=lambda x: len(x))
# a ['@', '??', '###']
# a.sort(key=lambda x: len(x), reverse=True) ['###', '??', '@']
#
# Что такое лямбда функция вы узнаете в дальнейшем (так же всегда
# есть сайт google). Для выполнения этого задания достаточно понять,
# на что надо заменить функцию len.
#
# Формат входных данных
# В первой строке N - количество студентов. Далее идет какое-то
# количество строк (не равное N) с результатами студентов в формате:
# student_id value. 0 <= student_id < N. Значения разделены пробелом.
# Ввод заканчивается #.
#
# Формат выходных данных
# Вывести отсортированные результаты студентов в одну строку.
# Сначала печатаются результаты лучшего по сумме баллов студента,
# потом второго и так далее. Результаты в одну строку
#
# Примеры
# Ввод	    Вывод
# 3           10 3 4 3 2
# 0 3
# 0 10
# 2 3
# 2 2
# 2 4
#
#
#
# Оставляем тот же подход, что было в lec06_arrays. В теории можно было
# использовать быструю сортировку или слиянием, но встроенная sorted
# по асимптотике делает то же самое:
# https://chat.openai.com/c/bc5c80c6-bf94-4fe9-b742-5aff4a4e4ad4
# Сдать решение задачи E-Результаты работы студентов в семестре
#
# Есть результаты работы студентов в семестре.
# Студентов выводить в порядке суммы их баллов.
# Требутеся вывести отсортированные результаты работ для каждого студента.
#
# Данные вводятся как: student_id value
#
# student_id принимает значения от 0 до N. value от 1 до 10
#
# Пример входных данных: 0 3 0 5 1 3 1 2
#
# Тут представленны данные о двух студента: 0 и 1.
# Сумма балов студента 0 - 8. Студента 1 - 5.
# Значит, сначала должны быть напечатаны результаты 0 студента, затем 1.
# Таким образом сначала надо вывести отсортированные результаты
# студента 0, затем студента 1:
#
# 5 3 3 2
#
# Напомним, что у list в питоне есть встроенный метод sort и есть
# функция sorted.
# У них есть параметр key, который определяет по каким значениям будет
# сортироваться объект.
# Например код ниже будет сортировать лист по длинне его элементов.
# Так же есть параметр reverse.
#
# a = ['###', '@', '??']
# a.sort(key=lambda x: len(x))
# a ['@', '??', '###']
# a.sort(key=lambda x: len(x), reverse=True)
# ['###', '??', '@']
#
# Что такое лямбда функция вы узнаете в дальнейшем (так же всегда есть
# сайт google). Для выполнения этого задания достаточно понять,
# на что надо заменить функцию len.
#
# Формат входных данных
# В первой строке N - количество студентов. Далее идет какое-то
# количество строк (не равное N) с результатами студентов в формате:
# student_id value. 0 <= student_id < N. Значения разделены пробелом.
# Ввод заканчивается #.
#
# Формат выходных данных
# Вывести отсортированные результаты студентов в одну строку.
# Сначала печатаются результаты лучшего по сумме баллов студента,
# потом второго и так далее.
# Результаты в одну строку
#
# Примеры
# Ввод	Вывод
# 3       10 3 4 3 2
# 0 3
# 0 10
# 2 3
# 2 2
# 2 4
# #

def create_input_data() -> list[int]:
    """Creates input data."""
    arr = []
    print("Input the data in the following format:\n"
          "- The first line is a number of students;\n"
          "- The last line is a line with a symbol #;\n"
          "- The lines between the first and last ones in the format:\n"
          "    student_id value,\n"
          "    0 <= student_id <= N (a number of students),\n"
          "    1 <= value <= 10.")
    while True:
        inp = input()
        if inp == '#':
            break
        elif len(inp.split()) == 1:
            arr.append(int(inp))
        else:
            arr.append([int(inp.split()[0]), int(inp.split()[1])])
    return arr


def find_sorted_ids(arr: list) -> list:
    """Finds sum of mark for every student and sort their ids."""
    arr_short = arr[1:]
    arr_st = [0] * arr[0]
    for el in arr_short:
        arr_st[el[0]] += el[1]
    indexed_arr = list(enumerate(arr_st))
    sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1], reverse=True)
    sorted_indexes = [tpl[0] for tpl in sorted_indexed_arr]
    return sorted_indexes


def sort_student_marks(arr: list, sorted_indexes: list) -> list:
    """Sorts the students marks."""
    sorted_marks = sorted(
        arr[1:],
        key=lambda x: (sorted_indexes.index(x[0]), -x[1])
    )
    return sorted_marks


def create_string_output(sorted_marks: list) -> str:
    """Returns sorted marks in one line."""
    string_output = " ".join([str(el[1]) for el in sorted_marks])
    return string_output


def main() -> None:
    input_data = create_input_data()
    sorted_indexes = find_sorted_ids(input_data)
    sorted_marks = sort_student_marks(input_data, sorted_indexes)
    string_output = create_string_output(sorted_marks)
    print(string_output)
    # return string_output


if __name__ == "__main__":
    main()
