from unittest import mock
import pytest

from ..ex03_avg_value import create_input_data, get_avg, get_avg2, main


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("4\n8\n5\n0\n", [4, 8, 5])
    ],
    ids=[
        '"4\n8\n5\n0\n", [4, 8, 5]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests the create_input_data functions."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([4, 8, 5], 5.67)
    ],
    ids=[
        '[4, 8, 5], 5.67'
    ]
)
def values(request):
    return request.param


def test_get_avg(values):
    """Tests the get_avg function."""
    input_data, expected = values
    actual = get_avg(input_data)
    assert actual == expected


def test_get_avg2(values):
    """Tests the get_avg2 function."""
    input_data, expected = values
    actual = get_avg2(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("4\n8\n5\n0\n",
         "Input a value.\nEvery value is a new line.\nUse 0 + Enter to quit.\n5.67\n")
    ],
    ids=[
        '"4\n8\n5\n0\n", '
        '"Input a value.\nEvery value is a new line.\nUse 0 + Enter to quit.\n5.67\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
