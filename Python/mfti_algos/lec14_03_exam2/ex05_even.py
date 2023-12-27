# Сдать решение задачи E-Сортировка: сначала чётные
#
# Дан список целых чисел. Отсортировать его так, чтобы сначала шли
# чётные по возрастанию, потом — нечётные во возрастанию.
#
# Формат входных данных
# Одна строка — список чисел через пробел. Длина списка не
# превосходит 10000.
#
# Формат выходных данных
# Отсортированный список чисел через пробел.
#
# Примеры
# Ввод	            Вывод
# 1 2 3 4 5           2 4 1 3 5
#
# Ввод	            Вывод
# 8 7 6 5 4 2 12      2 4 6 8 12 5 7
def create_input_data():
    inp = input("Input the data:\n")
    arr = [int(el) for el in inp.split()]
    return arr


def create_arrays(arr):
    even_arr = []
    odd_arr = []
    for el in arr:
        if el % 2 == 0:
            even_arr.append(el)
        else:
            odd_arr.append(el)
    return even_arr, odd_arr


def merge_sort(arr: list):
    """
    Sorts the given list using the merge sort algorithm.

    Args:
        A: The list to be sorted.

    Returns:
        None
    """
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return
    # Split the list into two halves
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    # Recursively sort the two halves
    merge_sort(left)
    merge_sort(right)
    # Merge the two halves
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        # Compare the elements from the two halves and add the smaller
        # one to the merged list
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add the remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    # Update the original list A with the merged values
    arr[:] = merged
    return merged


def sort_and_concat(even_arr, odd_arr):
    res = merge_sort(even_arr) + merge_sort(odd_arr)
    return " ".join(map(str, res))


def main():
    arr = create_input_data()
    print(arr)
    even_arr, odd_arr = create_arrays(arr)
    print(even_arr, odd_arr)
    res = sort_and_concat(even_arr, odd_arr)
    print(res)


if __name__ == "__main__":
    main()
