from unittest import mock

import pytest


from ..ex01_point_and_circle import main
from ..ex01_point_and_circle import compare_radius_and_point, create_input_data


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("0 0 1\n", [0, 0, 1]),
        ("-1 3 1\n", [-1, 3, 1])
    ],
    ids=[
        '"0 0 1\n", [0, 0, 1]',
        '"0 0 1\n", [-1, 3, 1]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests create_input_data()."""
    with mock.patch('builtins.input', return_value=input_data):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([0, 0, 1], "Yes"),
        ([-1, 3, 1], "No"),
        ([2, 2, 4], "Yes"),
    ],
    ids=[
        '[0, 0, 1], "Yes"',
        '[-1, 3, 1], "No"',
        '([2, 2, 4], "Yes")'
    ]
)
def test_compare_radius_and_point(input_data, expected):
    """Tests compare_radius_and_point."""
    actual = compare_radius_and_point(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("0 0 1\n", "Yes\n"),
        ("-1 3 1\n", "No\n"),
        ("2 2 4\n", "Yes\n")
    ],
    ids=[
        '"0 0 1\n", "Yes"',
        '"-1 3 1\n", "No"',
        '"2 2 4\n", "Yes"'
    ]
)
def test_main(input_date, expected, capsys):
    """Tests the main function."""
    with mock.patch("builtins.input", return_value=input_date):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
