from ..ex02_selection_sort import selection_sort


def test_ex02_selection_sort(arrays):
    """Tests the ex02_selection_sort."""
    input_data, expected = arrays
    actual = selection_sort(input_data)
    assert actual == expected
