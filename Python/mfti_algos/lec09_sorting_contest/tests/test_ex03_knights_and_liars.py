from unittest import mock

import pytest

from ..ex03_knights_and_liars import (
    create_input_data,
    count_with_first_status,
    compare_answers,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("4\n0 1 0 1\n", [4, 0, 1, 0, 1]),
        ("5\n0 1 0 1 0\n", [5, 0, 1, 0, 1, 0])
    ],
    ids=[
        '"4\n0 1 0 1\n", [4, 0, 1, 0, 1]',
        '"5\n0 1 0 1 0\n", [5, 0, 1, 0, 1, 0]'
    ]
)
def test_create_input_data(input_data, expected):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        actual = create_input_data()
        assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (([4, 0, 1, 0, 1], 1), 3),
        (([4, 0, 1, 0, 1], 0), 2),
        (([5, 0, 1, 0, 1, 0], 1), 3),
        (([5, 0, 1, 0, 1, 0], 0), 3),
        (([5, 1, 1, 1, 1, 1], 1), 6),
        (([5, 1, 1, 1, 1, 1], 0), 0)
    ],
    ids=[
        "([4, 0, 1, 0, 1], 1), 3",
        "([4, 0, 1, 0, 1], 0), 2",
        "(([5, 0, 1, 0, 1, 0], 1), 3)",
        "(([5, 0, 1, 0, 1, 0], 0), 3)",
        "(([5, 1, 1, 1, 1, 1], 1), 6)",
        "(([5, 1, 1, 1, 1, 1], 0), 0)"
    ]
)
def test_count_with_first_status(input_data, expected):
    actual = count_with_first_status(*input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ([4, 0, 1, 0, 1], 2),
        ([5, 0, 1, 0, 1, 0], 3),
        ([5, 1, 1, 1, 1, 1], 0)
    ],
    ids=[
        "[4, 0, 1, 0, 1], 2",
        "[5, 0, 1, 0, 1, 0], 3",
        "[5, 1, 1, 1, 1, 1], 0"
    ]
)
def test_compare_answers(input_data, expected):
    actual = compare_answers(input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        ("4\n0 1 0 1\n", "Input the data: \n2\n"),
        ("5\n0 1 0 1 0\n", "Input the data: \n3\n")
    ],
    ids=[
        '"4\n0 1 0 1\n", "Input the data: \n2\n"',
        '"5\n0 1 0 1 0\n", "Input the data: \n3\n"'
    ]
)
def test_create_input_data(input_data, expected, capsys):
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
