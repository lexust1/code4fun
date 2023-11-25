from unittest import mock

import pytest


from ..ex06_count_digit import (
    count_digits,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (["2", "123"], 1),
        (["3", "1323533"], 4)
    ],
    ids=[
        '["2", "123"], 1',
        '["3", "1323533"], 4'
    ]
)
def test_count_digits(input_data, expected):
    actual = count_digits(input_data)
    assert actual == expected


def test_main(capsys):
    input_data = "2 123"
    expected = "1\n"
    with mock.patch("builtins.input", return_value=input_data):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
