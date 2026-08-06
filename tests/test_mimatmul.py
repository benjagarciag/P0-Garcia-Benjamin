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


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    assert mimatmul(A, B) == [[58, 64], [139, 154]]


def test_matrices_rectangulares_mas_filas():
    A = [[1, 2], [3, 4], [5, 6]]
    B = [[1, 0, 1, 2], [0, 1, 1, 1]]
    assert mimatmul(A, B) == [[1, 2, 3, 4], [3, 4, 7, 10], [5, 6, 11, 16]]


def test_dimensiones_incompatibles_cuadradas():
    with pytest.raises(ValueError):
        mimatmul([[1, 2], [3, 4]], [[1, 0], [0, 1], [1, 1]])
