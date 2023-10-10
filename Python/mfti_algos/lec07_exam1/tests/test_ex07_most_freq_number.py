from unittest import mock
import pytest
from ..ex07_most_freq_number import (
    create_input_data,
    get_max,
    get_min,
    get_most_freq,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("4\n5\n5\n2\n5\n \n", (4, [5, 5, 2, 5]))
    ],
    ids=[
        '"4\n5\n5\n2\n5\n \n", (4, [5, 5, 2, 5])'
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
        ([1, 18, 32, 10, 15, 8, 19, 20], (32, 1)),
        ([1, 2, 3, 4, 10, 7, 10, 3], (10, 1))
    ],
    ids=[
        '[1, 18, 32, 10, 15, 8, 19, 20], (32, 1)',
        '[1, 2, 3, 4, 10, 7, 10, 3], (10, 1)'
    ]
)
def arrays(request):
    return request.param


def test_get_max(arrays):
    """Tests the get_max function."""
    input_data, expected = arrays
    actual = get_max(input_data)
    assert actual == expected[0]


def test_get_min(arrays):
    """Tests the get_min function."""
    input_data, expected = arrays
    actual = get_min(input_data)
    assert actual == expected[1]


@pytest.fixture(
    scope="module",
    params=[
        ((4, [5, 5, 2, 5]), 5),
        ((5, [5, 5, 2, 5, 4]), 5),
        ((12, [3, 25, 11, 21, 13, 7, 6, 8, 11, 11, 13, 22]), 11)
    ],
    ids=[
        '(4, [5, 5, 2, 5]), 5',
        '(5, [5, 5, 2, 5, 4]), 5',
        '(12, [3, 25, 11, 21, 13, 7, 6, 8, 11, 11, 13, 22]), 11'
    ]
)
def values(request):
    return request.param


def test_get_most_freq(values):
    """Tests the get_most_freq function."""
    input_data, expected = values
    actual = get_most_freq(*input_data)
    assert actual == expected


def test_get_most_freq_pw(values):
    """Tests the get_most_freq_pw function."""
    input_data, expected = values
    actual = get_most_freq(*input_data)
    assert actual == expected


@pytest.mark.parametrize(
     "input_data, expected",
     [
         (
             "12\n3\n25\n11\n21\n13\n7\n6\n8\n11\n11\n13\n22\n \n",
             "Input the values: the 1st element - the array length, others are the array elements. Use Whitespace + Enter to finish.\n11\n"
         )
     ],
     ids=[
         '12\n3\n25\n11\n21\n13\n7\n6\n8\n11\n11\n13\n22\n \n, '
         'Input the values: the 1st element - the array length, others are the array elements. Use Whitespace + Enter to finish.\n11\n'
     ]
 )
def test_main(input_data, expected, capsys):
    """Tests the main function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
