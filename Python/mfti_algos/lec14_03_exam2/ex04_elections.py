# Сдать решение задачи D-Выборы
#
# В одном государстве произошла реформа избирательной системы.
# С момента ее введения все избиратели государства делятся на K,
# возможно не равных по объему, групп. Внутри каждой группы проходит
# голосования "за" или "против". Если больше половины группы
# проголосовала "за", то общий голос группы считался "за", иначе -
# "против".
# Любой вопрос решался положительно, если больше половины групп
# проголосовало "за". Все бы ничего, но в такой системе есть недостаток.
# Партия, устроившая такую систему, получила возможность решать вопросы
# в свою пользу. Для этого они поместили в группы своих стронников.
# Например, для групп численностью 5, 5 и 7 человек достаточно иметь
# по три своих человека в первых двух группах. Всего 6 человек смогут
# решить вопрос в пользу партии. От Вас потребуется посчитать, какое
# минимальное количество сторонников надо иметь партии для заданного
# разбиения на группы.
#
# Формат входных данных
# На первой строке дано натуральное число K ≤ 10000. На следующей строке
# вводится K натуральных чисел через пробел.
#
# Формат выходных данных
# Одно число — минимальное количество сторонников партии.
#
# Примеры
# Ввод	Вывод
# 3       6
# 5 5 7
#
#
# Ввод	    Вывод
# 5           5
# 4 2 1 3 7
#
def create_input_data():
    arr = []
    print("Input the data")
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    arr[0] = int(arr[0])
    arr[1] = [int(el) for el in arr[1].split()]
    return arr


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


def choose_group(arr):
    # Sort elements in the group arr to choose groups that includes
    # minimal people
    if arr[0] % 2 == 0:
        group_num = arr[0] / 2 + 1
    else:
        group_num = int(arr[0] / 2) + 1
    inf_groups = merge_sort(arr[1])[ : group_num]
    return inf_groups


def count_people_group(groups):
    cnt = 0
    for group in groups:
        if group == 1:
            cnt += 1
        elif group % 2 == 0:
            cnt += int(group / 2) + 1
        elif group % 2 != 0:
            cnt += int(group / 2) + 1
    return cnt


def main():
    arr = create_input_data()
    print(arr)
    inf_groups = choose_group(arr)
    print(inf_groups)
    cnt = count_people_group(inf_groups)
    print(cnt)


if __name__ == "__main__":
    main()
