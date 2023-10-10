from unittest import mock
import pytest
from ..ex04_even_max import create_input_data, get_even_max, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1\n3\n5\n0\n", [1, 3, 5])
    ],
    ids=[
        '"1\n3\n5\n0\n", [1, 3, 5]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests the create_input_data function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1, 2, 4, 7, 4], 4),
        ([1, 3, 5, 0], 0)
    ],
    ids=[
        '[1, 2, 4, 7, 4], 4',
        '[1, 3, 5, 0], 0'
    ]
)
def test_get_evan_max(input_data, expected):
    """Tests the get_even_max function."""
    actual = get_even_max(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1\n2\n4\n7\n4\n0\n", "4\n"),
        ("1\n3\n5\n0\n", "0\n")
    ],
    ids=[
        '"1\n2\n4\n7\n4\n0\n", "4\n"',
        '1\n3\n5\n", "0\n"'
    ]
)
def test_main(input_data, expected, capsys):
    """Tests the main function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
