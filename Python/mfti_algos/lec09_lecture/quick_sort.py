# Quick Sort Algorithm (критичен Pivot)
# https://www.programiz.com/dsa/quick-sort

# QuickSort Complexity:
#
# Time Complexity:
# - Best Case: O(n log n) - Achieved when the pivot is the median,
# leading to a balanced partition.
# - Average Case: O(n log n) - With good pivot strategy, this is the
# typical performance.
# - Worst Case: O(n^2) - Occurs when the pivot is the smallest or
# largest element, leading to an unbalanced partition.
#
# Space Complexity:
# - O(log n) - Although QuickSort is an in-place sort, the call stack
# during recursion takes up O(log n) space.
#
# Note: To optimize QuickSort and prevent the worst-case scenario,
# strategies like "median-of-three" or randomized pivot selection can
# be used.
#
# Merge Sort works by dividing the unsorted list into n sublists, then
# repeatedly merges them to produce new sorted sublists until
# there's only one sublist remaining.
#
# QuickSort works by selecting a 'pivot' and then partitioning
# the array around the pivot

# По сути, в сортировке слиянием сперва разделяем все до последнего
# элемента и только по том, когда собираем все обратно на каждом шаге
# делаем сравнение, т.е. сортирующее действие.
# В быстрой сортировке иначе. Уже в ходе раскладывания значений на
# каждом шаге по трем кучкам, выполняется сортирующие действие. В конце
# нам остается только все собрать воедино.
def hoar_sort(A) -> None:
    """
    Sorts a list using the Hoare's partition scheme.

    Parameters:
        A (list): The list to be sorted.

    Returns:
        None: The list is sorted in-place.
    """
    # The base case.
    if len(A) <= 1:
        return
    # The recursive case.
    # Choose the first element as the barrier
    barrier = A[0]
    L = []  # Elements less than the barrier
    M = []  # Elements equal to the barrier
    R = []  # Elements greater than the barrier
    # Partition the list into L, M, R
    for x in A:
        if x < barrier:
            L.append(x)
            print(L, M, R)
        elif x == barrier:
            M.append(x)
            print(L, M, R)
        else:
            R.append(x)
            print(L, M, R)
    # Recursively sort the left and right partitions
    hoar_sort(L)
    hoar_sort(R)
    # Combine the sorted partitions
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


def main():
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    hoar_sort(array)
    print(array)


if __name__ == "__main__":
    main()
