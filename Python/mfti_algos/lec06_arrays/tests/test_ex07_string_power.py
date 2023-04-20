from unittest import mock

import pytest

from ..ex07_string_power import (
    create_input_data,
    choose_operation,
    count_power,
    count_root,
    main
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("abc\n3\n\n", ["abc", "3"]),
        ("abcabcabc\n-3\n\n", ["abcabcabc", "-3"])
    ],
    ids=[
        '"abc\n3\n\n", ["abc", "3"]',
        '"abcabcabc\n-3\n\n", ["abcabcabc", "-3"]'
    ]
)
def test_input_create_data(input_data, expected):
    """Tests the input_create_data function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


def test_choose_operation_negative_power():
    """Tests the choose operation function when the power is negative"""
    arr = ["abcabcabc", "-3"]
    with mock.patch("lec06_arrays.ex07_string_power.count_root", return_value="abc"):
        actual = choose_operation(arr)
        assert actual == "abc"


def test_choose_operation_positive_power():
    """Tests the choose operation function when the power is positive"""
    arr = ["abc", "3"]
    with mock.patch("lec06_arrays.ex07_string_power.count_power", return_value="abcabcabc"):
        actual = choose_operation(arr)
        assert actual == "abcabcabc"


def test_choose_operation_power_is_zero():
    """Tests the choose operation function when the power is zero."""
    arr = ["abc", "0"]
    actual = choose_operation(arr)
    assert actual == "Use positive or negative power, not zero."


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["abc", "3"], "abcabcabc"),
        (["abcd", "2"], "abcdabcd")
    ],
    ids=[
        '["abc", "3"], "abcabcabc"',
        '["abcd", "2"], "abcdabcd"'
    ]
)
def test_count_power(input_data, expected):
    actual = count_power(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["abcabcabc", "-3"], "abc"),
        (["abcabcabcabc", "-3"], "NO SOLUTION"),
        (["abcabcabcabcabcabc", "-3"], "abcabc"),
        (["abcabcabcaac", "-4"], "NO SOLUTION"),
        (["aacabcabcabc", "-4"], "NO SOLUTION"),
        (["abcabcaacabc", "-4"], "NO SOLUTION")
    ],
    ids=[
        '["abcabcabc", "-3"], "abc"',
        '["abcabcabcabc", "-3"], "NO SOLUTION"',
        '["abcabcabcabcabcabc", "-3"], "abcabc"',
        '["abcabcabcaac", "-4"], "NO SOLUTION"',
        '["aacabcabcabc", "-4"], "NO SOLUTION"',
        '["abcabcaacabc", "-4"], "NO SOLUTION"'
    ]
)
def test_count_root(input_data, expected):
    actual = count_root(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("abc\n3\n\n", "abcabcabc"),
        ("abcabcabc\n-3\n\n", "abc")
    ],
    ids=[
        '"abc\n3\n\n", "abcabcabc"',
        '"abcabcabc\n-3\n\n", "abc"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert expected in actual
