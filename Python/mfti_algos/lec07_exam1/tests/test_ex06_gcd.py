from unittest import mock
import pytest
from ..ex06_gcd import create_input_data, gcd, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("30\n18\n \n", [30, 18]),
        ("1071\n462\n \n", [1071, 462])
    ],
    ids=[
        '"30\n18\n \n", [30, 18]',
        '"1071\n462\n \n", [1071, 462]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([30, 18], 6),
        ([1071, 462], 21)
    ],
    ids=[
        '[30, 18], 6',
        '[1071, 462], 21'
    ]
)
def test_gcd(input_data, expected):
    actual = gcd(input_data)
    assert actual == expected


@pytest.mark.parametrize(
     "input_data, expected",
     [
         ("30\n18\n \n", "Whitespace + Enter to finish.\n6\n"),
         ("1071\n462\n \n", "Whitespace + Enter to finish.\n21\n")
     ],
     ids=[
         '"30\n18\n \n", "Whitespace + Enter to finish.\n6\n"',
         '"1071\n462\n \n", "Whitespace + Enter to finish.\n21\n"'
     ]
 )
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
