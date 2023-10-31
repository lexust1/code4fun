# The same as merge_sort.py but use more built-in functions
# (slicers, etc.) and merge two functions into one.


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

    # Create a new list to store the merged list
    C = [0] * (len(L) + len(R))
    # Initialize variables to track the indices of lists A, B, and C
    i = k = n = 0
    # Merge the lists A and B into the list C
    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            C[n] = L[i]
            i += 1
            print(L, R, C)  # Print the lists to debug the merging process
        else:
            C[n] = R[k]
            k += 1
            print(L, R, C)  # Print the lists to debug the merging process
        n += 1
    # Add the remaining elements of list A and B to the list C
    C[n:] = L[i:] + R[k:]
    print(L, R, C)  # Print the lists to debug the merging process
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
