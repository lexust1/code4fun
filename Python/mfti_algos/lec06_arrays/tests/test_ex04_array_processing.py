from unittest import mock

import pytest

from ..ex04_array_processing import (
    create_input_data,
    count_avg,
    count_avg_pw,
    find_max,
    find_max_pw,
    find_min,
    find_min_pw,
    count_remainders,
    count_remainders_pw,
    main
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1\n2\n3\n4\n5\n6\n#\n", [1, 2, 3, 4, 5, 6])
    ],
    ids=[
        '"1\n2\n3\n4\n5\n6\n#\n", [1, 2, 3, 4, 5, 6]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([1, 2, 3, 4, 5, 6], 3.5),
        ([0, 0, 0, 0, 0, 0], 0),
        ([1], 1),
        ([0], 0),
        ([1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 257.202),
        ([1, 1.1, 1.3], 1.133),
        ([0.000156, 0.06758538, 0.02956548], 0.032)
    ],
    ids=[
        '[1, 2, 3, 4, 5, 6], 3.5',
        '[0, 0, 0, 0, 0, 0], 0',
        '[1], 1',
        '[0], 0',
        '[1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 257.202',
        '[1, 1.1, 1.3], 3',
        '[0.000156, 0.06758538, 0.02956548], 0.032'
    ]
)
def values_avg(request):
    return request.param


def test_count_avg(values_avg):
    """Tests the count_avg function."""
    input_data, expected = values_avg
    actual = count_avg(input_data)
    assert actual == expected


def test_count_avg_pw(values_avg):
    """Tests the count_avg_pw function."""
    input_data, expected = values_avg
    actual = count_avg_pw(input_data)
    assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([1, 2, 3, 4, 5, 6], 6),
        ([6, 5, 4, 3, 2, 1], 6),
        ([1, 2, 6, 3, 4, 5], 6),
        ([1, 2, 6, 3, 4, 6], 6),
        ([1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 1000),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1], 1)
    ],
    ids=[
        '[1, 2, 3, 4, 5, 6], 6',
        '[6, 5, 4, 3, 2, 1], 6',
        '[1, 2, 6, 3, 4, 5], 6',
        '[1, 2, 6, 3, 4, 6], 6',
        '[1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 1000',
        '[0, 0, 0, 0, 0, 0, 0, 0, 0], 0',
        '[1, 1, 1, 1, 1], 1'
    ]
)
def values_max(request):
    return request.param


def test_find_max(values_max):
    """Tests the find_max function."""
    input_data, expected = values_max
    actual = find_max(input_data)
    assert actual == expected


def test_find_max_pw(values_max):
    """Tests the find_max_pw function."""
    input_data, expected = values_max
    actual = find_max_pw(input_data)
    assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([1, 2, 3, 4, 5, 6], 1),
        ([6, 5, 4, 3, 2, 1], 1),
        ([1, 2, 6, 3, 4, 5], 1),
        ([1, 2, 6, 3, 4, 6], 1),
        ([1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 1.1),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1], 1)
    ],
    ids=[
        '[1, 2, 3, 4, 5, 6], 6',
        '[6, 5, 4, 3, 2, 1], 6',
        '[1, 2, 6, 3, 4, 5], 6',
        '[1, 2, 6, 3, 4, 6], 6',
        '[1.1, 1.25, 1000, 325.127, 678.3122, 10, 10.5, 31.3235], 1000',
        '[0, 0, 0, 0, 0, 0, 0, 0, 0], 0',
        '[1, 1, 1, 1, 1], 1'
    ]
)
def values_min(request):
    return request.param


def test_find_min(values_min):
    """Tests the find_min function."""
    input_data, expected = values_min
    actual = find_min(input_data)
    assert actual == expected


def test_find_min_pw(values_min):
    """Tests the find_min_pw function."""
    input_data, expected = values_min
    actual = find_min_pw(input_data)
    assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        ([1, 2, 3, 4, 5, 6], 3),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90], 90),
        ([1, 2, 3, 1, 2, 3, 1, 2, 3], 0),
        ([4, 5, 6, 4, 5, 6, 4, 5, 6], 9),
        ([4, 5, 6], 3),
        ([1.1, 1.3, 1.3], 1.1)
    ],
    ids=[
        '[1, 2, 3, 4, 5, 6], 3',
        '[10, 20, 30, 40, 50, 60, 70, 80, 90], 90',
        '[1, 2, 3, 1, 2, 3, 1, 2, 3], 0',
        '[4, 5, 6, 4, 5, 6, 4, 5, 6], 9',
        '[4, 5, 6], 3',
        '[1.1, 1.3, 1.3], 1.1'
    ]
)
def values_rmd(request):
    return request.param


def test_count_remainders(values_rmd):
    """Tests the count_remainders function."""
    input_data, expected = values_rmd
    actual = count_remainders(input_data)
    assert actual == expected


def test_count_remainders_pw(values_rmd):
    """Tests the count_remainders_pw function."""
    input_data, expected = values_rmd
    actual = count_remainders_pw(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1\n2\n3\n4\n5\n6\n#\n", "3.5 6 1 3\n")
    ],
    ids=[
        '"1\n2\n3\n4\n5\n6\n#\n", "3.5 6 1 3\n"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert expected in actual
