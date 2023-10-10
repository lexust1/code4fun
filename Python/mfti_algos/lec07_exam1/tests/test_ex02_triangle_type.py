from unittest import mock
import pytest


from ..ex02_triangle_type import create_input_data, get_triangle_type, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("3\n4\n5\n \n", [3, 4, 5])
    ],
    ids=[
        '"3\n4\n5\n \n", [3, 4, 5]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests teh create_input_data function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([3, 2, 9], "impossible"),
        ([9, 12, 15], "right"),
        ([10, 13, 15], "acute"),
        ([8, 11, 15], "obtuse")

    ],
    ids=[
        '[3, 2, 9], "impossible"',
        '[9, 12, 15], "right"',
        '[10, 13, 15], "acute"',
        '[8, 11, 15], "obtuse"'
    ]
)
def test_get_triangle_type(input_data, expected):
    """Tests teh get_triangle_type function."""
    actual = get_triangle_type(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("3\n2\n9\n \n", "impossible"),
        ("9\n12\n15\n \n", "right"),
        ("10\n13\n15\n \n", "acute"),
        ("8\n11\n15\n \n", "obtuse")
    ],
    ids=[
        '("3\n2\n9\n \n", "impossible")',
        '("9\n12\n15\n \n", "right")',
        '("10\n13\n15\n \n", "acute")',
        '("8\n11\n15\n \n", "obtuse")'
    ]
)
def test_main(input_data, expected):
    """Tests the main function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = main()
        assert actual == expected
