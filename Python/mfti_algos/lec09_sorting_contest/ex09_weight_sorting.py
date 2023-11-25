# Сдать решение задачи I-Матпомощь
#
# Задача I: Матпомощь
# Студентов надо построить в шеренгу от самого легкого до самого
# тяжелого. Кто мало весит - тем выдать матпомощь..
# При одинаковом весе сначала идет студент с большим ростом (тощий).
#
# Формат входных данных
# Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел
# (float) через пробел - рост в метрах и вес в килограммах одного
# студента.
#
# Формат результата
# Рост и вес (печатать рост с точностью до сантиметров, а вес -
# до граммов) по одному студенту на строку от первого студента в шеренге
# к последнему
#
# Примеры
# Входные данные
# 3
# 1.8 70
# 1.75 70
# 1.8 69.5
# Результат работы
# 1.80 69.500
# 1.80 70.000
# 1.75 70.000
def create_input_data() -> list:
    """
    Creates input data by prompting the user to enter data.

    Returns:
        list: a list of values.
    """
    print("Input the data: ")
    arr = []
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    return arr


def sort_values_pw(arr):
    """
    Sorts a list using the built-in python sorted function.

    Args:
        arr (list): List of strings representing height-weight tuples.

    Returns:
        str: String representing the sorted height-weight tuples.
    """
    # Get the length of the list
    length = int(arr[0])
    # Parse the height-weight tuples from the input list
    h_w_tuples = [
        (float(el.split()[0]), float(el.split()[1])) for el in arr[1:]
    ]
    # Sort the height-weight tuples
    h_w_tuples_sorted = sorted(h_w_tuples, key=lambda x: (x[1], -x[0]))
    # Convert the sorted tuples to a string representation
    sorted_values = ""
    for el in h_w_tuples_sorted:
        sorted_values += f"{el[0]:.2f} {el[1]:.3f}\n"
    return sorted_values


def sort_values(arr):
    """
    Sorts a list of tuples based on two criteria and returns the
    sorted values.

    Args:
        arr (list): A list of strings where the first element is an
            integer and the rest are space-separated floats.

    Returns:
        str: A string containing the sorted values.

    """
    # Extract the length of the list from the first element
    length = int(arr[0])
    # Convert the remaining strings into tuples of floats
    h_w_tuples = [
        (float(el.split()[0]), float(el.split()[1])) for el in arr[1:]
    ]
    # Sort the tuples based on the first element (height)
    h_w_tuples = merge_sort(h_w_tuples, 0)
    # Sort the tuples based on the second element (weight)
    h_w_tuples_sorted = merge_sort(h_w_tuples, 1)
    # Format the sorted tuples as a string
    sorted_values = ""
    for el in h_w_tuples_sorted:
        sorted_values += f"{el[0]:.2f} {el[1]:.3f}\n"
    return sorted_values


def merge_sort(arr, pos):
    """The merge sort."""
    # The base case
    if len(arr) <= 1:
        return
    # The recursive case.
    # Divide into 2 halves
    middle = len(arr) // 2
    left = arr[: middle]
    right = arr[middle :]
    # Sort two halves.
    merge_sort(left, pos)
    merge_sort(right, pos)
    # Merge two halves.
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][pos] < right[j][pos]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    arr[:] = merged
    return arr


def main():
    # Test
    # arr = ['3', '1.8 70', '1.75 70', '1.8 69.5']
    # arr = ['8', '1.75 70', '1.75 70', '1.8 70', '1.8 69.5', '1.8 90',
    #         '1.75 30', '1.75 100', '1.8 30']
    arr = create_input_data()
    print(arr)
    print(sort_values_pw(arr))
    print(sort_values(arr))


if __name__ == "__main__":
    main()
