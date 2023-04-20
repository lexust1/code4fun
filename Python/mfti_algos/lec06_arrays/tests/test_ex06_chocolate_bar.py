from unittest import mock

import pytest

from ..ex06_chocolate_bar import (
    input_chocolate_length,
    count_number_of_ways,
    main
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("0", 0),
        ("1", 1),
        ("5", 5)
    ],
    ids=[
        '"0", 0',
        '"0", 0',
        '"0", 0'
    ]
)
def test_input_chocolate_length(input_data, expected):
    with mock.patch("builtins.input", return_value=input_data):
        actual = input_chocolate_length()
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (0, "It is impossible to divide the chocolate bar because there is no chocolate."),
        (1, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 1"),
        (2, 3),
        (3, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 3"),
        (4, 11),
        (5, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 5"),
        (6, 41),
        (7, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 7"),
        (8, 153),
        (9, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 9"),
        (10, 571)
    ],
    ids=[
        '"0", "It is impossible to divide the chocolate bar because there is no chocolate."',
        '1, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 1"',
        '2, 3',
        '3, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 3"',
        '4, 11',
        '5, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 5"',
        '6, 41',
        '7, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 7"',
        '8, 153',
        '9, "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 9"',
        '10, 571'
    ]
)
def test_count_number_of_ways(input_data, expected):
    actual = count_number_of_ways(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("4", "11\n"),
        ("5", "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 5\n")
    ],
    ids=[
        '"4", 11',
        '"5", "It is impossible to divide the chocolate bar because the amount of chocolate pieces is odd: 3 x 5"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected