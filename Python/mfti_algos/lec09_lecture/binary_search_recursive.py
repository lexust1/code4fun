# Бинарные поиск (O(log(n)))
# Binary search is an efficient algorithm for finding an item from a
# SORTED list of items. It works by repeatedly dividing the portion of
# the list that could contain the item in half until you have narrowed
# down the possible locations to just one.
#
# The binary search algorithm has a time complexity of
# O(log(n)), where n is the number of elements in the array.
def binary_search(array: list, x: int, low: int, high: int) -> int:
    """
    Perform binary search to find the index of a given element in a
    sorted list.

    Parameters:
    - array (list): The sorted list in which to search.
    - x (int): The element to search for.
    - low (int): The starting index of the section to consider.
    - high (int): The ending index of the section to consider.

    Returns:
    - int: The index of the element x if found, otherwise -1.
    """
    # The base case: Check if the search interval is valid
    if low <= high:
        # Calculate the middle index of the current interval
        mid = low + (high - low) // 2
        # Check if the element at the middle index is the target
        if array[mid] == x:
            return mid
        # If the element at the middle is greater than the target,
        # search in the left half
        elif array[mid] > x:
            return binary_search(array, x, low, mid - 1)
        # Otherwise, search in the right half
        else:
            return binary_search(array, x, mid + 1, high)
    # If the search interval is not valid, the element is not in the
    # list
    else:
        return -1


def main():
    array = [2, 3, 6, 7, 7, 10, 10, 11, 12, 13, 19, 21]
    print(binary_search(array, 13, 0, len(array) - 1))
    print(binary_search(array, 5, 0, len(array) - 1))
    print(binary_search(array, 23, 0, len(array) - 1))
    print(binary_search(array, -5, 0, len(array) - 1))


if __name__ == "__main__":
    main()
