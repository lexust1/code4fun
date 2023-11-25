from unittest import mock

import pytest


from ..ex05_bracket_expressions import (
    check_brackets,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("()", "YES"),
        (")(", "NO"),
        ("()(())()", "YES"),
        ("()(())(", "NO"),
        ("()(()()", "NO"),
        (")", "NO")
    ],
    ids=[
        '"()", "YES"',
        '")(", "NO"',
        '"()(())()", "YES"',
        '"()(())(", "NO"',
        '"()(()()", "NO"',
        '")", "NO"'
    ]
)
def test_check_brackets(input_data, expected):
    actual = check_brackets(input_data)
    assert actual == expected


def test_main(capsys):
    input_data = "()(())()"
    expected = "YES\n"
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
