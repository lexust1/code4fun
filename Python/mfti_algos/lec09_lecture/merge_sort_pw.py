# The same as merge_sort.py but use more built-in functions
# (slicers, etc.)

def merge(A: list, B: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        A: The first sorted list.
        B: The second sorted list.

    Returns:
        C: The merged sorted list.
    """
    # Create a new list to store the merged list
    C = [0] * (len(A) + len(B))
    # Initialize variables to track the indices of lists A, B, and C
    i = k = n = 0
    # Merge the lists A and B into the list C
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            print(A, B, C)  # Print the lists to debug the merging process
        else:
            C[n] = B[k]
            k += 1
            print(A, B, C)  # Print the lists to debug the merging process
        n += 1
    # Add the remaining elements of list A and B to the list C
    C[n:] = A[i:] + B[k:]
    print(A, B, C)  # Print the lists to debug the merging process
    return C  # Return the merged sorted list


def merge_sort(A: list):
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
    # The recursive case.
    # Split the list into two halves
    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    # Recursively sort the two halves
    merge_sort(L)
    merge_sort(R)
    # Merge the sorted halves
    C = merge(L, R)
    # Copy the merged list back to the original list
    A[:] = C


def main():
    # A = [1, 5, 10, 12]
    # B = [6, 9]
    # print(merge(A, B))
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()
    