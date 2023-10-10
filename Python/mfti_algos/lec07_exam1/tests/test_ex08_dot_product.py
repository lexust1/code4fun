import pytest
from ..ex08_dot_product import dot_product, dot_product2, dot_product3


@pytest.fixture(
    scope="module",
    params=[
        ((3, [1, 2, 3], [1, 2, 3]), 14),
        ((3, [1, 2, 3], [4, 5, 6]), 32)
    ],
    ids=[
        "(3, [1, 2, 3], [1, 2, 3]), 14",
        "(3, [1, 2, 3], [4, 5, 6]), 32"
    ]
)
def values(request):
    return request.param


def test_dot_product(values):
    """Tests the dot_product function."""
    input_data, expected = values
    actual = dot_product(*input_data)
    assert actual == expected


def test_dot_product2(values):
    """Tests the dot_product function."""
    input_data, expected = values
    actual = dot_product2(input_data[1], input_data[2])
    assert actual == expected


def test_dot_product3(values):
    """Tests the dot_product function."""
    input_data, expected = values
    actual = dot_product3(input_data[1], input_data[2])
    assert actual == expected
