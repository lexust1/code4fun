# Counting sort has a time complexity of O(n + k),
# where n is the number of elements in the input array and k is the
# range of input values. The algorithm requires additional space
# for the count array and the output array, both of which have
# a size of k.
# https://www.programiz.com/dsa/counting-sort


def counting_sort_simple(arr):
    """Does counting sort.

    Does counting sort but does not preserve the order of equal values.
    """
    min_val = min(arr)
    max_val = max(arr)
    freq_arr = [0] * (max_val - min_val + 1)

    for el in arr:
        freq_arr[el - min_val] += 1
        print(freq_arr)

    sorted_arr = []
    for idx in range(len(freq_arr)):
        if freq_arr[idx] != 0:
            sorted_arr.append(str(idx + min_val) * freq_arr[idx])
            print(sorted_arr)

    output = "".join(sorted_arr)
    print(output)

    return output


def counting_sort(arr):
    """Does the full count sort.

    Does the full count sort preserving the order of equal values.
    """
    min_val = min(arr)
    max_val = max(arr)
    count_arr = [0] * (max_val - min_val + 1)
    # Find the frequency array, how many times every value repeats.
    for el in arr:
        count_arr[el - min_val] += 1
    print(count_arr)
    # Find the cummulative array
    # Before the cumulative count step:
    # The count array [1, 2, 2, 0, 1, 0, 0, 1] represents the frequency
    # of each element before computing the cumulative counts.
    # For example, there is one occurrence of 1, two occurrences of 2,
    # and so on.
    # After the cumulative count step:
    # The count array [1, 3, 5, 5, 6, 6, 6, 7] represents the
    # cumulative counts. Each element at index i in the count array
    # denotes the number of elements less than or equal to the value
    # represented by index i. For example, there are 3 elements less
    # than or equal to 2, 5 elements less than or equal to 3, and so on.
    for idx in range(1, len(count_arr)):
        count_arr[idx] += count_arr[idx - 1]
    print(count_arr)
    # The final output array.
    output = [0] * len(arr)
    # for el in arr[::-1]:
    #     output[count_arr[el - min_val] - 1] = el
    #     count_arr[el - min_val] -= 1
    #     print(output)
    i = len(arr) - 1
    while i >= 0:
        output[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
        i -= 1
    # Copy the sorted elements of our array to the original array.
    arr[:] = output
    print(arr)
    return arr


def main():
    arr = [3, 2, 2, 3, 7, 2, 4, 4, 2]
    print(arr)
    output = counting_sort(arr)
    # print_sorted_arr(freq_arr)


if __name__ == "__main__":
    main()
