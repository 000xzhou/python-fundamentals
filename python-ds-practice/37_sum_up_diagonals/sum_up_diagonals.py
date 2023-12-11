def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # (0,0)(1,1)(2,2)
    # (0,2)(1,1)(2,0)
    sum_x = 0
    sum_y = 0
    for i in range(len(matrix)):
        sum_x += matrix[i][i]
        sum_y += matrix[i][len(matrix)-1-i]
    return sum_x + sum_y
