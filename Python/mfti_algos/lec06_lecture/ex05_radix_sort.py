# Radix sort is a non-comparative sorting algorithm that sorts
# integers by examining their digits from the least significant
# digit (LSD) to the most significant digit (MSD).
# It is often used to sort numbers in a fixed-size representation,
# such as binary or decimal numbers.
#
# Radix sort has a time complexity of O(k * n), where n is the number
# of elements and k is the average number of digits.
# It is efficient when the range of values to be sorted is small
# compared to the number of elements, but it can be less efficient
# for large ranges or when the number of digits is very high.

# https://www.programiz.com/dsa/radix-sort

def counting_sort(arr, place):
    """Does the count sort."""
    count_arr = [0] * 10
    # Find the frequency array, how many times every value repeats.
    for el in arr:
        idx = el // place
        count_arr[idx % 10] += 1
        # print(count_arr)
    # Find the cummulative array.
    for idx in range(1, 10):
        count_arr[idx] += count_arr[idx - 1]
        # print(count_arr)
    # The final output array.
    output = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        idx = arr[i] // place
        output[count_arr[idx % 10] - 1] = arr[i]
        count_arr[idx % 10] -= 1
        i -= 1
    # Copy the sorted elements of our array to the original array.
    arr[:] = output
    print(arr)


def radix_sort(arr):
    """Does radix sort."""
    max_val = max(arr)
    place = 1
    while max_val // place > 0:
        # Use the count_sorting algo for every digit (place).
        counting_sort(arr, place)
        place *= 10
    return arr


def main():
    # arr = [170, 45, 75, 90, 802, 24, 2, 66]
    arr = [121, 432, 564, 23, 1, 45, 788]
    radix_sort(arr)


if __name__ == "__main__":
    main()
