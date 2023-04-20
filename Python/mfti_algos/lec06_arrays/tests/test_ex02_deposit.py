from unittest import mock

import pytest

from ..ex02_deposit import create_input_data, trunc_copeck, find_year, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1000 12 2000\n", [1000, 12, 2000]),
        ("2000 3 6000\n", [2000, 3, 6000]),
    ],
    ids=[
        '"1000 12 2000\n", [1000, 12, 2000]',
        '"2000 3 6000\n", [2000, 3, 6000]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests the create_input_data function."""
    with mock.patch("builtins.input", return_value=input_data):
        actual = create_input_data()
    assert actual == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (1000, 1000),
        (1000.12, 1000.12),
        (1000.1234, 1000.12),
    ],
    ids=[
        "1000, 1000",
        "1000.12, 1000.12",
        "1000.1234, 1000.12"
    ]
)
def test_trunc_copeck(x, expected):
    """Tests the trunc_copeck function."""
    actual = trunc_copeck(x)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1000, 12, 2000], 7),
        ([1000, 12, 1000], 0),
        ([1450.93, 12, 2000], 3),
        ([1000, 1.5, 3000], 74)
    ],
    ids=[
        "[1000, 12, 2000], 7",
        "[1000, 12, 1000], 0",
        "[1450.93, 12, 2000], 3",
        "[1000, 1.5, 3000], 74"
    ]
)
def test_find_year(input_data, expected):
    actual = find_year(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1000 12 2000\n", "7\n"),
        ("1000 12 1000\n", "0\n"),
        ("1450.93 12 2000\n", "3\n"),
        ("1000 1.5 3000\n", "74\n")
    ],
    ids=[
        '"1000 12 2000\n", "7\n"',
        '"1000 12 1000\n", "0\n"',
        '"1450.93 12 2000\n", "3\n"',
        '"1000 1.5 3000\n", "74\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
