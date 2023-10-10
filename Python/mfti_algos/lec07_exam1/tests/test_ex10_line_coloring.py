from unittest import mock
import pytest
from ..ex10_line_coloring import (
    create_input_data,
    parse_data,
    get_colored_lines,
    main
)


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (
            "3\n4\n6\n2\n7\n19\n6\n13\n15\n1\n2\n5\n14\n \n",
            [3, 4, 6, 2, 7, 19, 6, 13, 15, 1, 2, 5, 14]
        )
    ],
    ids=[
        '"3\n4\n6\n2\n7\n19\n6\n13\n15\n1\n2\n5\n14\n \n", '
        '[3, 4, 6, 2, 7, 19, 6, 13, 15, 1, 2, 5, 14]'
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
        (
            [3, 4, 6, 2, 7, 19, 6, 13, 15, 1, 2, 5, 14],
            (3, [4, 6, 2, 7, 19, 6, 13, 15, 1], 2, [5, 14])
        ),
    ],
    ids=[
        "[3, 4, 6, 2, 7, 19, 6, 13, 15, 1, 2, 5, 14], (3, [4, 6, 2, 7, 19, 6, 13, 15, 1], 2, [5, 14])"
    ]
)
def arrays(request):
    return request.param


def test_parse_data(arrays):
    """Tests the parse_data function."""
    input_data, expected = arrays
    actual = parse_data(input_data)
    assert actual == expected


@pytest.fixture(
    scope="module",
    params=[
        (
            (3, [4, 6, 2, 7, 19, 6, 13, 15, 1], 2, [5, 14]), [2, 1]
        ),
    ],
    ids=[
        "(3, [4, 6, 2, 7, 19, 6, 13, 15, 1], 2, [5, 14]), [2, 1]"
    ]
)
def tuples(request):
    return request.param


def test_get_colored_lines(tuples):
    """Tests the get_colored_lines function."""
    input_data, expected = tuples
    actual = get_colored_lines(*input_data)
    assert actual == expected


@pytest.mark.parametrize(
    argnames="input_data, expected",
    argvalues=[
        (
            "3\n4\n6\n2\n7\n19\n6\n13\n15\n1\n2\n5\n14\n \n",
            "Input every value on a new line."
            "Whitespace + Enter to finish.\n[2, 1]\n"
        )
    ],
    ids=[
        '"3\n4\n6\n2\n7\n19\n6\n13\n15\n1\n2\n5\n14\n \n", [2, 1]'
    ]
)
def test_main(input_data, expected, capsys):
    """Tests the main function."""
    with mock.patch("builtins.input", side_effect=input_data.split("\n")):
        main()
        actual = capsys.readouterr().out
        assert actual == expected
