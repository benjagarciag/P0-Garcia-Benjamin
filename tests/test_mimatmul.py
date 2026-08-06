import pytest

from src.mimatmul import mimatmul


def test_matrices_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert mimatmul(A, B) == [[19, 22], [43, 50]]


def test_matriz_1x1():
    assert mimatmul([[3]], [[4]]) == [[12]]


def test_dimensiones_incompatibles():
    with pytest.raises(ValueError):
        mimatmul([[1, 2]], [[1, 2, 3]])
