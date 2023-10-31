# The same but two functions. Maybe, it is a more clear.
def merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left (list): The left half of the list to be merged.
        right (list): The right half of the list to be merged.

    Returns:
        merged: The merged and sorted list.
    """
    # Initialize variables
    i, j = 0, 0
    merged = []
    # Compare elements from the two halves and add the smaller one to
    # the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add the remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(A: list) -> None:
    """
    Sorts the given list using the merge sort algorithm.

    Args:
        A: The list to be sorted.

    Returns:
        None
    """
    # The base case.
    if len(A) <= 1:
        return
    # Split the list into two halves
    middle = len(A) // 2
    left = A[:middle]
    right = A[middle:]
    # The recursive case
    # Recursively sort the two halves
    merge_sort(left)
    merge_sort(right)
    # Merge the two sorted halves
    merged = merge(left, right)
    # Update the original list with the merged result
    A[:] = merged


def main():
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()