from unittest import mock

import pytest

from ..ex03_max_serial_ones import (
    create_input_data,
    count_max,
    count_max_pw,
    main
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("4\n1\n1\n0\n1\n", [4, 1, 1, 0, 1]),
        (
            "10\n1\n1\n0\n1\n1\n1\n0\n1\n0\n1\n",
            [10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
        ),
        ("1\n1\n", [1, 1])
    ],
    ids=[
        '"4\n1\n1\n0\n1\n", [4, 1, 1, 0, 1]',
        '"10\n1\n1\n0\n1\n1\n1\n0\n1\n0\n1\n", '
        '[10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]',
        '"1\n1\n", [1, 1]'
    ]
)
def test_create_input_data(input_data, expected):
    """Tests the create_input_data function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([4, 1, 1, 0, 1], 2),
        ([10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1], 3),
        ([10, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1], 3),
        ([10, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0], 3),
        ([1, 1], 1),
        ([1, 0], 0),
        ([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10),
        ([10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    ],
    ids=[
        "[4, 1, 1, 0, 1], 2",
        "[10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1], 3",
        "[10, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1], 3)",
        "[10, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0], 3",
        "[1, 1], 1",
        "([1, 0], 0)",
        "[10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10",
        "[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10"
    ]
)
def values(request):
    return request.param


def test_count_max(values):
    """Tests the test_count_max function."""
    input_data, expected = values
    actual = count_max(input_data)
    assert actual == expected


def test_count_max_pw(values):
    """Tests the count_max_pw function."""
    input_data, expected = values
    actual = count_max_pw(input_data)
    assert actual == expected

@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("4\n1\n1\n0\n1\n",
         "Initial array: [4, 1, 1, 0, 1]\n"
         "The first method: 2\n"
         "The second method: 2\n"
         ),
        (
            "10\n1\n1\n0\n1\n1\n1\n0\n1\n0\n1\n",
            "Initial array: [10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]\n"
            "The first method: 3\n"
            "The second method: 3\n"
        )
    ],
    ids=[
        '"4\n1\n1\n0\n1\n", '
        '"Initial array: [4, 1, 1, 0, 1]\n'
        'The first method: 2\n'
        'The second method: 2\n"',
        '"10\n1\n1\n0\n1\n1\n1\n0\n1\n0\n1\n",'
        '"Initial array: [10, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]\n'
        'The first method: 3\n'
        'The second method: 3\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
    assert actual == expected
