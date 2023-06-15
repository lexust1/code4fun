from ..ex01_insertion_sort import insertion_sort


def test_ex01_insertion_sort(arrays):
    """Tests the ex01_insertion_sort."""
    input_data, expected = arrays
    actual = insertion_sort(input_data)
    assert actual == expected


