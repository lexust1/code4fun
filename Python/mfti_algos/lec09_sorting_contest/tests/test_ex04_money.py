from unittest import mock

import pytest


from ..ex04_money import (
    create_input_data,
    count_money,
    count_money_pw,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("10\n1\n1\n", [10, 1, 1])
    ],
    ids=[
        '"10\n1\n1\n", [10, 1, 1]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", return_value=input_data):
        actual = create_input_data()
        assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([10, 1, 1], 91),
        ([5, 1, 2], 161)
    ],
    ids=[
        "[10, 1, 1], 91",
        "[5, 1, 2], 161",
    ]
)
def values(request):
    return request.param


def test_count_money(values):
    input_data, expected = values
    actual = count_money(input_data)
    assert actual == expected


def test_count_money_pw(values):
    input_data, expected = values
    actual = count_money_pw(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("10\n1\n1\n", "Input the price, weekly price change, and a num of weeks: \n91\n"),
        ("5\n1\n2\n", "Input the price, weekly price change, and a num of weeks: \n161\n")
    ],
    ids=[
        '"10\n1\n1\n", "Input the price, weekly price change, and a num of weeks: \n91\n"',
        '"5\n1\n2\n", "Input the price, weekly price change, and a num of weeks: \n161\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
