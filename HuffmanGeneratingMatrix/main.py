import math
import numpy as np
from Constans import Constans as ct


def read_input():
    try:
        n = int(input("Insert n: "))
        if n<3:
            raise Exception
        return n
    except Exception:
        print("\nError occurred!\n")
        return read_input()


def create_matrix(value, rows, columns):
    if value == 0:
        return np.zeros((rows, columns), dtype=np.int16)
    elif value == 1:
        return np.ones((rows, columns), dtype=np.int16)
    else:
        return np.full((rows, columns), value)


def create_matrix_b(n):
    if n == 3:
        return ct.B_THREE

    n-=1
    pow = int(math.pow(2, n-1)-1)
    b_n_minus_one = create_matrix_b(n)
    zero_quadratic_matrix = create_matrix(0, pow, pow)

    first_row = np.concatenate((b_n_minus_one, create_matrix(0, pow, 1)), axis=1)
    first_row = np.concatenate((first_row, zero_quadratic_matrix), axis=1)
    second_row = np.concatenate((create_matrix(0, 1, pow), create_matrix(1, 1, 1)), axis=1)
    second_row = np.concatenate((second_row, create_matrix(0, 1, pow)), axis=1)
    third_row = np.concatenate((b_n_minus_one, create_matrix(1, pow, 1)), axis=1)
    third_row = np.concatenate((third_row, zero_quadratic_matrix), axis=1)

    b_n = np.concatenate((first_row, second_row), axis=0)
    b_n = np.concatenate((b_n, third_row), axis=0)

    return b_n


def create_matrix_g(n):
    if n == 2:
        return ct.G_TWO

    n-=1
    pow = int(math.pow(2, n)-1)
    pow_minus_n = int(math.pow(2, n)-n-1)

    g_n_minus_one = create_matrix_g(n)
    b_n = create_matrix_b(n+1)
    identity_matrix = np.identity(pow, dtype=np.int16)

    first_row = np.concatenate((g_n_minus_one, create_matrix(0, pow_minus_n, 1)), axis=1)
    first_row = np.concatenate((first_row, create_matrix(0, pow_minus_n, pow)), axis=1)

    second_row = np.concatenate((b_n, create_matrix(1, pow, 1)), axis=1)
    second_row = np.concatenate((second_row, identity_matrix), axis=1)

    g_n = np.concatenate((first_row, second_row), axis=0)

    return g_n


def __main__():
    n = read_input()

    b_n = create_matrix_b(n)
    print(f'B({n}):')
    print(b_n)

    g_n = create_matrix_g(n)
    print(f'\nG({n}):')
    print(g_n)

__main__()