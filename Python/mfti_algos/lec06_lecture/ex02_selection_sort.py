# Selection Sort is a straightforward sorting technique. You repeatedly
# find the smallest (or largest) element in the unsorted part of the
# list and swap it with the element at the beginning of the unsorted
# part. This way, you gradually build up the sorted portion of the list
# until all elements are in the right order.
#
# The algorithm works in-place and has a time complexity of O(n^2)
#
# Example:
# [4, 2, 5, 1, 3]
# [1, 2, 5, 4, 3]
# [1, 2, 3, 4, 5]

# https://www.programiz.com/dsa/selection-sort
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=1576s (There is an
# error here because the elements are swapped every time, it is not
# the way.)
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=3959s

def selection_sort(arr):
    """Does selection sort."""
    for idx in range(0, len(arr) - 1):
        min_idx = idx
        for k in range(idx + 1, len(arr)):
            if arr[k] < arr[min_idx]:
                min_idx = k
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        print(arr)
    return arr


def main():
    array = [4, 2, 5, 1, 3]
    print(selection_sort(array))


if __name__ == "__main__":
    main()
