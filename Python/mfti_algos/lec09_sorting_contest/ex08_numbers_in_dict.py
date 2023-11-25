# Сдать решение задачи H-Числа в словарном порядке
#
# Напечатайте входную последовательность натуральных чисел,
# отсортировав ее по возрастанию сначала единиц, потом десятков,
# потом сотен и тп.
#
# Входные данные
#
# Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих
# 30000, через пробел.
#
# Выходные данные
#
# Числа по возрастанию единиц, при равных единиц - по возрастанию
# десятков, при равных единицах и десятков - по возрастанию сотен и тп.
#
# Примеры
#
# Вход                Выход
#
# 5                   3 23 123 43 5
# 5 23 3 43 123
#
#
#

def create_input_data():
    """
    Prompts the user to input data and returns a list of inputs.

    Returns:
        arr: A list containing the user inputs.
    """
    print("Input the data: ")
    arr = []
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    return arr


def sort_values_pw(arr: list) -> str:
    """
    Sorts the numbers in the given array in ascending order based on
    the last three digits of each number using the built-in function.

    Args:
        arr (list): The input array containing the numbers.

    Returns:
        str: A string representation of the sorted numbers separated
        by a space.
    """
    # Extract the numbers from the array
    numbers = [int(el) for el in arr[1].split()]
    # Sort the numbers based on the last three digits
    sort_numbers = sorted(
        numbers,
        key=lambda x: (x % 10, x % 100, x % 1000)
    )
    return " ".join([str(el) for el in sort_numbers])


def sort_values(arr: list) -> str:
    """
    Sorts the values in the array based on their different positions.

    Args:
        arr (list): The input array containing values to be sorted.

    Returns:
        str: The sorted values as a string.

    """
    # Convert the string of numbers to a list of integers
    numbers = [int(el) for el in arr[1].split()]
    # Create tuples of the numbers with their remainders when divided
    # by 1000, 100, and 10
    tuples = [(num % 1000, num % 100, num % 10) for num in numbers]
    # Sort the tuples based on each position in ascending order
    for pos in range(3):
        tuples = merge_sort(tuples, pos)
    # Convert the sorted tuples back to a string
    sorted_arr = " ".join([str(el[0]) for el in tuples])
    return sorted_arr


def merge_sort(arr: list, pos: int) -> list | None:
    """
    Sorts a list of elements in ascending order using the merge sort
    algorithm.

    Args:
        arr (list): The list of elements to be sorted.
        pos (int): The position in the tuple to compare while
            merging.
    Returns:
        list | None: The sorted list. If the input list is empty or
        has only one element, returns None.
    """
    # The base case.
    if len(arr) <= 1:
        return
    # Recursive case.
    # Split the list into 2 halves.
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    # Sort two halves.
    merge_sort(left, pos)
    merge_sort(right, pos)
    # Merge two halves.
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i][pos] <= right[j][pos]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    arr[:] = merged
    return merged


def main():
    # arr = ["5", "5 23 3 43 123"]
    # arr = ["6", "5 23 3 43 871 123"]
    arr = create_input_data()
    print(arr)
    print(sort_values_pw(arr))
    print(sort_values(arr))


if __name__ == "__main__":
    main()
