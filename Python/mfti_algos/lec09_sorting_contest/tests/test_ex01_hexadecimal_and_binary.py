from unittest import mock

import pytest


from ..ex01_hexadecimal_and_binary import (
    create_input_data,
    hex_to_bin,
    bin_to_hex,
    exclusive_or,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("1 23", ["1", "23"]),
        ("f0 0f", ["f0", "0f"])
    ],
    ids=[
        '"1 23", ["1", "23"]',
        '"f0 0f", ["f0", "0f"]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", return_value=input_data):
        actual = create_input_data()
        assert expected == actual


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("1", "0001"),
        ("f0", "11110000")
    ],
    ids=[
        '"1", "0001"',
        '"f0", "11110000"'
    ]
)
def test_hex_to_bin(input_data, expected):
    actual = hex_to_bin(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("0001", "1"),
        ("11110000", "f0")
    ],
    ids=[
        '"0001", "1"',
        '"11110000", "f0"'
    ]
)
def test_bin_to_hex(input_data, expected):
    actual = bin_to_hex(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (["1111", "1110"], "0001"),
        (["11110000", "1110"], "11111110")
    ],
    ids=[
        '["1111", "1110"], "0001"',
        '["11110000", "1110"], "11111110"'
    ]
)
def test_exclusive_or(input_data, expected):
    actual = exclusive_or(*input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("1 23", "22\n"),
        ("f0 0f", "ff\n")
    ],
    ids=[
        '"1 23", "22\n"',
        '"f0 0f", "ff\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert expected == actual

