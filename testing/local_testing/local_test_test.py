# test_math_operations.py

import pytest
import add_function


result_index = [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (5, -3, 2),
    (1, 1, 2)
]

@pytest.mark.parametrize("a, b, expected_result", result_index)


def test_add(a, b, expected_result):
    assert add_function.add(a, b) == expected_result


