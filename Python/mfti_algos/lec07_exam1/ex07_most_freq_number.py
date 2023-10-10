# Сдать решение задачи G-Самое частое число
#
# На вход программе подается массив чисел.Необходимо найти число,
# которое чаще всего встречается в массиве. Гарантируется, что такое
# число одно.
#
# Формат входных данных
# В первой строке задается число N , длина массива, далее идут N
# чисел -- элементы массива. Все числа больше 0 и меньше 100. Каждое
# число вводится с новой строки.
#
# Формат выходных данных
# Одно число, которое встречается наибольшее количество раз.
#
# Примеры
# Ввод	Вывод
# 4       5
# 5
# 5
# 2
# 5
# It reminds a little the counting sort. Length can be used for range
# during iteration but not a pythonic way. It is easier to get elements
# iterating through array directly.
def create_input_data() -> tuple:
    """Creates a list of numbers."""
    arr = []
    cnt_inps = 0
    length = 0
    print(
        "Input the values: "
        "the 1st element - the array length, "
        "others are the array elements. "
        "Use Whitespace + Enter to finish."
    )
    while True:
        cnt_inps += 1
        inp = input()
        if inp == " ":
            break
        if cnt_inps == 1:
            length = int(inp)
        else:
            arr.append(int(inp))
    return length, arr


def get_max(arr) -> int:
    """Finds the max of array."""
    max_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el
    return max_el


def get_min(arr) -> int:
    """Finds the min of array."""
    min_el = arr[0]
    for el in arr:
        if el < min_el:
            min_el = el
    return min_el


def get_most_freq(length, arr) -> int:
    """Finds the most frequent element in the array w/o max, min..."""
    # Find the smallest and the largest elements in the input array.
    min_el = get_min(arr)
    max_el = get_max(arr)
    # Create a frequency array. The purpose is to count the occurrences
    # of each element in the input array.
    freq_arr = [0] * (max_el - min_el + 1)
    # Set the initial values for the maximum frequency and its index.
    max_freq_el = 0
    most_freq_el = 0
    # Find the element with the highest frequency.
    # for el in arr:  # a more pythonic way, see an example below.
    for el_idx in range(length):
        el = arr[el_idx]
        freq_arr[el - min_el] += 1
        # Check if the current element's frequency is higher than
        # the maximum frequency recorded so far.
        if freq_arr[el - min_el] > max_freq_el:
            # If so, update the maximum frequency and the most frequent
            # element.
            max_freq_el = freq_arr[el - min_el]
            most_freq_el = el
    return most_freq_el


def get_most_freq_pw(arr) -> int:
    """Finds the most frequent element in the array w/ max, min..."""
    # Find the smallest and the largest elements in the input array.
    min_el = min(arr)
    max_el = max(arr)
    # Create a frequency array. The purpose is to count the occurrences
    # of each element in the input array.
    freq_arr = [0] * (max_el - min_el + 1)
    # Set the initial values for the maximum frequency and its index.
    max_freq_el = 0
    most_freq_el = 0
    # Find the element with the highest frequency.
    for el in arr:
        freq_arr[el - min_el] += 1
        # Check if the current element's frequency is higher than
        # the maximum frequency recorded so far.
        if freq_arr[el - min_el] > max_freq_el:
            # If so, update the maximum frequency and the most frequent
            # element.
            max_freq_el = freq_arr[el - min_el]
            most_freq_el = el
    return most_freq_el


def main():
    """The main function."""
    print(get_most_freq(*create_input_data()))


if __name__ == "__main__":
    main()
