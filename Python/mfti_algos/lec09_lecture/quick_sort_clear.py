# The same as quick_sort but use two functions to implement in-place
# sorting (it is a more efficient way).
# function to find the partition position
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
        print(array)
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            print(array)
    # Swap the pivot with the element just before i to place the pivot
    # in its correct sorted position.
    array[low], array[i - 1] = array[i - 1], array[low]
    # Return the new position of the pivot element.
    return i - 1


def quick_sort(array: list, low: int, high: int) -> None:
    """
    Sorts an array using the quicksort algorithm.

    Parameters:
    - array: The array to be sorted.
    - low: The starting index of the array or subarray to be sorted.
    - high: The ending index of the array or subarray to be sorted.

    Returns:
    None
    """
    if low < high: # The base case when low == high
        # Partition the array and get the pivot index
        pivot_idx = partition(array, low, high)
        print("Pivot_idx, low, high", pivot_idx, low, high)
        # Recursively sort the two subarrays before and after the pivot
        quick_sort(array, low, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, high)
        print(array[low : pivot_idx - 1])
        print(array[pivot_idx + 1 : high])


def main():
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    quick_sort(array, 0, len(array) - 1)
    print(array)


if __name__ == "__main__":
    main()
