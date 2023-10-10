from unittest import mock

import pytest


from ..ex01_truck import create_input_data, estimate_logistics


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("5\n2\n1\n2\n1\n3\n6\n3\n \n", [5, 2, 1, 2, 1, 3, 6, 3])
    ],
    ids=[
        '"5\n2\n1\n2\n1\n3\n6\n3\n \n", [5, 2, 1, 2, 1, 3, 6, 3]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([5, 2, 1, 2, 1, 3, 6, 3], "NO"),
        ([1, 1, 5, 10, 5, 10, 10, 10], "NO"),
        ([1, 1, 5, 10, 5, 10, 12, 12], "YES"),
        ([1, 2, 1, 2, 1, 3, 4, 10], "YES"),
        ([1, 2, 1, 2, 2, 3, 3, 10], "YES"),
        ([1, 2, 1, 2, 2, 3, 3, 2], "NO")
    ],
    ids=[
        '[5, 2, 1, 2, 1, 3, 6, 3], "NO"',
        '[1, 1, 5, 10, 5, 10, 10, 10], "NO"',
        '[1, 1, 5, 10 ,5, 10, 11, 11], "YES"',
        '[1, 2, 1, 2, 1, 3, 1, 10], "YES"',
        '[1, 2, 1, 2, 2, 3, 3, 10], "YES"',
        '[1, 2, 1, 2, 2, 3, 3, 2], "NO"'
    ]
)
def test_estimate_logistics(input_data, expected):
    actual = estimate_logistics(input_data)
    assert actual == expected
