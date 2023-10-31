# Clear the code.
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


def main():
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()
