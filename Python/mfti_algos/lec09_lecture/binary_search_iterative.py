# Бинарные поиск (O(log(n)))
# Binary search is an efficient algorithm for finding an item from a
# SORTED list of items. It works by repeatedly dividing the portion of
# the list that could contain the item in half until you have narrowed
# down the possible locations to just one.
#
# The binary search algorithm has a time complexity of
# O(log(n)), where n is the number of elements in the array.
#
# This iterative approach has the same time complexity O(log n)
# as the recursive approach for binary search. However, it has a
# space complexity of O(1), making it more space-efficient than
# the recursive version when considering the call stack.
def binary_search(array: list, x: int, low: int, high: int) -> int:
    """
    Perform binary search to find the index of a given element in
    a sorted list.

    Parameters:
    - array (list): The sorted list in which to search.
    - x (int): The element to search for.
    - low (int): The starting index of the section to consider.
    - high (int): The ending index of the section to consider.

    Returns:
    - int: The index of the element x if found, otherwise -1.
    """
    # Continue the loop as long as the search interval is valid
    while low <= high:
        # Calculate the middle index of the current interval
        mid = low + (high - low) // 2
        # Check if the element at the middle index is the target
        if array[mid] == x:
            return mid
        # If the element at the middle is less than the target,
        # update 'low' to narrow the search to the right half
        elif array[mid] < x:
            low = mid + 1
        # Otherwise, update 'high' to narrow the search to the left half
        else:
            high = mid - 1
    # If the loop completes without returning, the element is not in
    # the list
    return -1


def main():
    array = [2, 3, 6, 7, 7, 10, 10, 11, 12, 13, 19, 21]
    print(binary_search(array, 13, 0, len(array) - 1))
    print(binary_search(array, 5, 0, len(array) - 1))
    print(binary_search(array, 23, 0, len(array) - 1))
    print(binary_search(array, -5, 0, len(array) - 1))


if __name__ == "__main__":
    main()
