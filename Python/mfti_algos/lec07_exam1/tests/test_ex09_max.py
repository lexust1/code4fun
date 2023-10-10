from unittest import mock
import pytest
from ..ex09_max import (
    create_input_data,
    clear_data,
    clear_data_pw,
    get_max,
    get_max_pw,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("1\n2\n3\n4\n5\n6\n0\n", [1, 2, 3, 4, 5, 6])
    ],
    ids=[
        '"1\n2\n3\n4\n5\n6\n0\n", [1, 2, 3, 4, 5, 6]'
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
        ([1, 2, 3, 4, 5, 6], [1]),
        ([1, 5, 2, 15, 373, 232, 43, 21, 5433, 5312], [1, 5, 2, 15, 373])
    ],
    ids=[
        "[1, 2, 3, 4, 5, 6], [1]",
        "[1, 5, 2, 15, 373, 232, 43, 21, 5433, 5312], [1, 5, 2, 15, 373])"
    ]
)
def arrays(request):
    return request.param


def test_clear_data(arrays):
    """Tests the clear_data function."""
    input_data, expected = arrays
    actual = clear_data(input_data)
    assert actual == expected


def test_clear_data_pw(arrays):
    """Tests the clear_data_pw function."""
    input_data, expected = arrays
    actual = clear_data_pw(input_data)
    assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([1], 1),
        ([1, 5, 2, 15, 373], 373)
    ],
    ids=[
        "[1], 1",
        "[1, 5, 2, 15, 373], 373"
    ]
)
def cleared_arrays(request):
    return request.param


def test_get_max(cleared_arrays):
    """Tests the get_max function."""
    input_data, expected = cleared_arrays
    actual = get_max(input_data)
    assert actual == expected


def test_get_max_pw(cleared_arrays):
    """Tests the get_max_pw function."""
    input_data, expected = cleared_arrays
    actual = get_max_pw(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (
            "1\n2\n3\n4\n5\n6\n0\n",
            "Input a list of values. Every value is in a new line."
            "Use 0 + Enter to finish.\n1\n"
        )
    ],
    ids=[
        ('"1\n2\n3\n4\n5\n6\n0\n", 1')
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
