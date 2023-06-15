# Bubble Sort is a simple sorting algorithm where you compare adjacent
# elements in the list and swap them if they are in the wrong order.
# The larger (or smaller) elements "bubble" towards the end
# (or beginning) of the list with each pass.
# This process is repeated until the entire list is sorted.

# The algorithm works in-place and has a time complexity of O(n^2)
# in the worst case.

# Example
# [4, 2, 5, 1, 3]
# [2, 4, 5, 1, 3]
# [2, 4, 1, 5, 3]
# [2, 4, 1, 3, 5]
# [2, 1, 4, 3, 5]
# [2, 1, 3, 4, 5]
# [1, 2, 3, 4, 5]

# https://www.programiz.com/dsa/bubble-sort
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=2059s
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=4083s

def bubble_sort(arr):
    """Does bubble sort."""
    for bypass in range(0, len(arr) - 1):
        for k in range(0, len(arr) - bypass - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
            print(arr)
    return arr


def main():
    arr = [4, 2, 5, 1, 3]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
