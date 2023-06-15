# Insertion sort is a simple sorting algorithm that works by dividing
# an array into a sorted and an unsorted region. It iteratively takes
# elements from the unsorted region and places them in the correct
# position within the sorted region.
#
# The algorithm works in-place and has a time complexity of O(n^2)
# in the worst case.
#
# Example:
# [4, 2, 5, 1, 3]
# [2, 4, 5, 1, 3]
# [2, 4, 1, 5, 3]
# [2, 1, 4, 5, 3]
# [1, 2, 4, 5, 3]
# [1, 2, 4, 3, 5]
# [1, 2, 3, 4, 5]

# https://www.programiz.com/dsa/insertion-sort
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=1228s
# https://www.youtube.com/watch?v=NLq7nB9bV0M&t=3575s

def insertion_sort(arr):
    """Does insertion sort."""
    for idx in range(1, len(arr)):
        key = idx
        while key > 0 and arr[key] < arr[key - 1]:
            arr[key], arr[key - 1] = arr[key - 1], arr[key]
            key -= 1
            print(arr)
    return arr


def main():
    array = [4, 2, 5, 1, 3]
    print(insertion_sort(array))


if __name__ == "__main__":
    main()
