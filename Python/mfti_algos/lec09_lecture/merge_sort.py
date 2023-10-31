# Merge Sort Algorithm (Сортировка слиянием, "разделяй и властвуй")
# https://www.programiz.com/dsa/merge-sort

# Merge Sort Complexity Analysis:
#
# Time Complexity:
#   - Best Case:    O(n log n)
#   - Average Case: O(n log n)
#   - Worst Case:   O(n log n)
#   The reasoning for this time complexity is as follows:
#   - The list is divided in half with each recursive call, leading
#   to log n divisions
#     (where n is the length of the list).
#   - Merging the divided lists requires linear time, i.e., O(n).
#   - Therefore, the overall time complexity for the process is
#   O(n log n).
#
# Space Complexity:
#   - O(n)
#   Merge sort requires additional space to store the two halves during
#   the merging process.
#   This means that in terms of space, it's not as efficient as some
#   in-place sorting algorithms.
#   The space complexity arises from the auxiliary space used for
#   the left and right
#   sub-arrays and any other temporary storage used during the merge
#   process.
#
# Note: Merge sort guarantees a time complexity of O(n log n) for
# all cases, making it one of the most efficient sorting algorithms
# in terms of time. However, there is a space overhead
# due to its non-in-place nature.
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
            n += 1
            print(A, B, C)  # Print the lists to debug the merging process
        else:
            C[n] = B[k]
            k += 1
            n += 1
            print(A, B, C)  # Print the lists to debug the merging process
    # Add the remaining elements of list A to the list C
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
        print(A, B, C)  # Print the lists to debug the merging process
    # Add the remaining elements of list B to the list C
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
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
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    # Recursively sort the two halves
    merge_sort(L)
    merge_sort(R)
    # Merge the sorted halves
    C = merge(L, R)
    # Copy the merged list back to the original list
    for i in range(len(A)):
        A[i] = C[i]


def main():
    # A = [1, 5, 10, 12]
    # B = [6, 9]
    # print(merge(A, B))
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()
