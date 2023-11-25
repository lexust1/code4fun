from unittest import mock

import pytest


from ..ex02_binary_representation import (
    dec_to_bin
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("5", 2),
        ("159", 6)
    ],
    ids=[
        '"5", 2',
        '"159", 6'
    ]
)
def test_dec_to_bin(input_data, expected):
    actual = dec_to_bin(input_data)
    assert expected == actual
