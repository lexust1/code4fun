from ..ex03_bubble_sort import bubble_sort


def test_ex03_bubble_sort(arrays):
    """Tests test_ex03_bubble_sort(arrays)."""
    input_data, expected = arrays
    actual = bubble_sort(input_data)
    assert actual == expected
