from ..ex04_counting_sort import counting_sort


def test_ex04_counting_sort(arrays):
    """Tests test_ex04_counting_sort(arrays)."""
    input_data, expected = arrays
    actual = counting_sort(input_data)
    assert actual == expected