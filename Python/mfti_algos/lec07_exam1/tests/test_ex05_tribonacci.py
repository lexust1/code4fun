from unittest import mock
import pytest
from ..ex05_tribonacci import get_tribonacci_idx, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (10, 7),
        (0, 2),
        (13, 8)
    ],
    ids=[
        "10, 7",
        "0, 2",
        "13, 8"
    ]
)
def test_get_tribonacci_idx(input_data, expected):
    """Test the get_tribonacci_idx2 function."""
    actual = get_tribonacci_idx(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (10, 7),
        (0, 2),
        (13, 8)
    ],
    ids=[
        "10, 7",
        "0, 2",
        "13, 8"
    ]
)
def test_get_tribonacci_idx2(input_data, expected):
    """Test the get_tribonacci_idx function."""
    actual = get_tribonacci_idx(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("10\n", "The index: 7\n"),
        ("0\n", "The index: 2\n"),
        ("13\n", "The index: 8\n")
    ],
    ids=[
        '"10\n", "The index: 7\n"',
        '"0\n", "The index: 2\n"',
        '"13\n", "The index: 8\n"'
    ]
)
def test_main(input_data, expected, capsys):
    """Test the main function."""
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected

