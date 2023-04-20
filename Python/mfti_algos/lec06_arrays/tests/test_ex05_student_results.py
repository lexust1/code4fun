from unittest import mock

import pytest

from ..ex05_student_results import (
    create_input_data,
    find_sorted_ids,
    sort_student_marks,
    create_string_output,
    main
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "3\n0 3\n0 10\n2 10\n2 9\n2 4\n0 3\n1 8\n1 8\n#\n",
            [3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]]
        ),
        (
            "1\n0 3\n#\n", [1, [0, 3]]
        )
    ],
    ids=[
        '"3\n0 3\n0 10\n2 10\n2 9\n2 4\n0 3\n1 8\n1 8\n#\n",'
        '[3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]]',
        '"1\n0 3\n#\n", [1, [0, 3]]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([3, [0, 3], [1, 2], [2, 10]], [2, 0, 1]),
        ([3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]], [2, 0, 1]),
        ([3, [0, 3], [0, 10], [2, 3], [2, 2], [2, 4]], [0, 2, 1]),
        ([3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]], [2, 0, 1]),
        ([1, [0, 3]], [0])
    ],
    ids=[
        "([3, [0, 3], [1, 2], [2, 10]], [2, 0, 1]",
        "[3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]], [2, 0, 1]",
        "[3, [0, 3], [0, 10], [2, 3], [2, 2], [2, 4]], [0, 2, 1]",
        "[3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]],",
        "[1, [0, 3]], [0]"
    ]
)
def test_find_sorted_ids(input_data, expected):
    actual = find_sorted_ids(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data1, input_data2, expected",
    [
        (
            [3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]],
            [2, 0, 1],
            [[2, 10], [2, 9], [2, 4], [0, 10], [0, 3], [0, 3], [1, 8], [1, 8]]
        ),
        (
            [1, [0, 3]], [0], [[0, 3]]
        )
    ],
    ids=[
        "[3, [0, 3], [0, 10], [2, 10], [2, 9], [2, 4], [0, 3], [1, 8], [1, 8]],"
        "[2, 0, 1],"
        "[[2, 10], [2, 9], [2, 4], [0, 10], [0, 3], [0, 3], [1, 8], [1, 8]]",
        "[1, [0, 3]], [0], [[0, 3]]"
    ]
)
def test_sort_student_marks(input_data1, input_data2, expected):
    actual = sort_student_marks(input_data1, input_data2)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            [[2, 10], [2, 9], [2, 4], [0, 10], [0, 3], [0, 3], [1, 8], [1, 8]],
            "10 9 4 10 3 3 8 8"
        ),
        (
            [[0, 3]], "3"
        )
    ],
    ids=[
        '[[2, 10], [2, 9], [2, 4], [0, 10], [0, 3], [0, 3], [1, 8], [1, 8]],'
        '"10 9 4 10 3 3 8 8"',
        '[[0, 3]], "3"'
    ]
)
def test_create_string_output(input_data, expected):
    actual = create_string_output(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "3\n0 3\n0 10\n2 10\n2 9\n2 4\n0 3\n1 8\n1 8\n#\n",
            "10 9 4 10 3 3 8 8"
        ),
        (
            "1\n0 3\n#\n", "3"
        )
    ],
    ids=[
        '"3\n0 3\n0 10\n2 10\n2 9\n2 4\n0 3\n1 8\n1 8\n#\n",'
        '"10 9 4 10 3 3 8 8"',
        '"1\n0 3\n#\n", "3"'
    ]
)
def test_main(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert expected in actual
