# Сдать решение задачи G-Отсортированные символы
#
# Напечатайте входную строку, отсортировав ее по возрастанию ASCII
# кода символов.
#
# Входные данные
#
# Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку
# сортировать не нужно. Все, что находится после первой точки -
# игнорировать.
#
# Выходные данные
#
# Отсортированная строка с точкой на конце.
#
# Примеры
#
# Вход                    Выход
#
# qwe Rty5, yu! Mama.     !,5MRaaemqtuwyy.
def sorted_chars_pw(inp: str) -> str:
    chars = ""
    for char in inp:
        if char == ".":
            break
        if char != " ":
            chars += char
    return "".join(sorted(chars)) + "."


def chars_to_codes(inp: str) -> list:
    codes = []
    for char in inp:
        if char == ".":
            break
        if char != " ":
            codes.append(ord(char))
    return codes


def insertion_sort(codes: list) -> str:
    for idx in range(1, len(codes)):
        key = idx
        while key > 0 and codes[key] < codes[key - 1]:
            codes[key], codes[key - 1] = codes[key - 1], codes[key]
            key -= 1
    return "".join([chr(code) for code in codes]) + "."


def selection_sort(codes: list) -> str:
    for idx in range(0, len(codes) - 1):
        min_idx = idx
        for k in range(idx + 1, len(codes)):
            if codes[k] < codes[min_idx]:
                min_idx = k
        codes[idx], codes[min_idx] = codes[min_idx], codes[idx]
    return "".join([chr(code) for code in codes]) + "."


def buble_sort(codes: list) -> str:
    for bypass in range(0, len(codes) - 1):
        for k in range(0, len(codes) - bypass - 1):
            if codes[k] > codes[k + 1]:
                codes[k], codes[k + 1] = codes[k + 1], codes[k]
    return "".join([chr(code) for code in codes]) + "."


def counting_sort(codes: list) -> str:
    min_val = min(codes)
    max_val = max(codes)
    count_codes = [0] * (max_val - min_val + 1)
    # Find the frequency array
    for code in codes:
        count_codes[code - min_val] += 1
    # Find the cummulative array
    for idx in range(1, len(count_codes)):
        count_codes[idx] += count_codes[idx - 1]
    # The final output
    output = [0] * len(codes)
    i = len(codes) - 1
    while i >= 0:
        output[count_codes[codes[i] - min_val] - 1] = codes[i]
        count_codes[codes[i] - min_val] -= 1
        i -= 1
    codes[:] = output
    return "".join([chr(code) for code in codes]) + "."


def merge_sort(A: list):
    """
    Sorts the given list using the merge sort algorithm.

    Args:
        A: The list to be sorted.

    Returns:
        None
    """
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if len(A) <= 1:
        return
    # Split the list into two halves
    middle = len(A) // 2
    left = A[:middle]
    right = A[middle:]
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
    A[:] = merged
    return "".join([chr(code) for code in A]) + "."


def partition(array: list, low: int, high: int) -> int:
    """
    Partition the array around a pivot element.

    Example walkthrough of the `partition` function:

    Given array = [3, 8, 2, 5, 1], and calling partition(array, 0, 4):

    1. Pivot is 3; start i at index 1.
    2. For j = 1 (element = 8): No action as 8 > 3.
    3. For j = 2 (element = 2): Swap with i (i remains 2, array
        becomes [3, 2, 8, 5, 1]).
    4. For j = 3 (element = 5): No action as 5 > 3.
    5. For j = 4 (element = 1): Swap with i (i becomes 3, array
        becomes [3, 2, 1, 5, 8]).
    6. Post-loop: Swap pivot with i-1 element (array
        becomes [1, 2, 3, 5, 8]).
    7. Pivot (3) is now at index 2.

    Final array: [1, 2, 3, 5, 8], and the function returns 2.

    Args:
        array (list): The array to be partitioned.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.

    Returns:
        int: The final position of the pivot element.
    """
    # Choose the leftmost element as the pivot.
    pivot = array[low]
    # Initialize the pointer i to the position right after the pivot.
    i = low + 1
    # Traverse through elements in the current segment of the array.
    for j in range(i, high + 1):
        # If the current element is smaller than or equal to the pivot,
        # swap it with the element at position i.
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    # Swap the pivot with the element just before i to place the pivot
    # in its correct sorted position.
    array[low], array[i - 1] = array[i - 1], array[low]
    # Return the new position of the pivot element.
    return i - 1


def quick_sort(array: list, low: int, high: int) -> str:
    """
    Sorts an array using the quicksort algorithm.

    Parameters:
    - array: The array to be sorted.
    - low: The starting index of the array or subarray to be sorted.
    - high: The ending index of the array or subarray to be sorted.

    Returns:
    str
    """
    if low < high:  # The base case when low == high
        # Partition the array and get the pivot index
        pivot_idx = partition(array, low, high)
        # Recursively sort the two subarrays before and after the pivot
        quick_sort(array, low, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, high)
    return "".join([chr(code) for code in array]) + "."


def main():
    inp = "qwe Rty5, yu! Mama"
    print("The data to sort: ", inp)
    print("Built-in sort: ", sorted_chars_pw(inp))
    codes = chars_to_codes(inp)
    print(codes)
    print("Insertion sort: ", insertion_sort(codes))
    print("Selection sort: ", selection_sort(codes))
    print("Bubble sort: ", buble_sort(codes))
    print("Counting sort: ", counting_sort(codes))
    print("Merge sort: ", merge_sort(codes))
    print("Quick sort: ", quick_sort(codes, 0, len(codes) - 1))


if __name__ == "__main__":
    main()
