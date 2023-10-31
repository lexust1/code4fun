# Проверят отсортирован массив или нет за O(n) = O(len(A))
def check_sorted(A, ascending=True):
    """
    Check if the given list A is sorted.

    Parameters:
    - A (list): The list to be checked.
    - ascending (bool, optional): If True, checks for ascending order.
                                  If False, checks for descending order.
                                  Default is True.

    Returns:
    - bool: True if the list is sorted in the specified order, False
        otherwise.
    """
    N = len(A)  # Get the length of the list A
    # Assume the list is sorted until proven otherwise
    flag = True
    # Determine the sign for the comparison based on the desired order
    # ascending or not.
    sign = 2 * int(ascending) - 1
    # Iterate through all the elements of the list except the last one
    for i in range(0, N - 1):
        # Compare adjacent elements based on the desired order
        if sign * A[i] > sign * A[i + 1]:
            # If any pair of elements is out of order, set flag to
            # False and exit the loop
            flag = False
            break
    # Return the result
    return flag


def main():
    array1 = [2, 3, 6, 7, 7, 10, 10, 11, 12, 13, 19, 21]
    array2 = [2, 3, 6, 7, 7, 10, 10, 11, 12, 19, 13, 21]
    array3 = [21, 13, 19, 12, 11, 10, 10, 7, 7, 6, 3, 2]
    array4 = [21, 19, 13, 12, 11, 10, 10, 7, 7, 6, 3, 2]
    print(check_sorted(array1))
    print(check_sorted(array2))
    print(check_sorted(array1, ascending=False))
    print(check_sorted(array2, ascending=False))
    print(check_sorted(array3))
    print(check_sorted(array4))
    print(check_sorted(array3, ascending=False))
    print(check_sorted(array4, ascending=False))


if __name__ == "__main__":
    main()
