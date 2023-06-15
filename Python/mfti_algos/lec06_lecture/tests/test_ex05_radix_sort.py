from ..ex05_radix_sort import radix_sort


def test_ex05_radix_sort(arrays):
    """Tests test_ex05_radix_sort(arrays)."""
    input_data, expected = arrays
    actual = radix_sort(input_data)
    assert actual == expected
