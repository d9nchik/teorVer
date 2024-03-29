from math import factorial, e, sqrt, pi, ceil, floor

import numpy as np
from scipy.optimize import fsolve
from scipy.special import erf


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)


def theorem_bernuli(k: int, n: int, p: float) -> float:
    """
    :param k: number of successful attempt
    :param n: number of attempts
    :param p: successful probability
    :return: probability
    """
    q = 1 - p
    return combination(k, n) * (p ** k) * (q ** (n - k))


def most_possible_success_variants(n: int, p: float):
    """
    :param n: number of attempts
    :param p: successful probability
    :return: most possible success variants
    """
    q = 1 - p
    first = ceil(n * p - q)
    second = floor(n * p + p)
    return [x for x in range(first, second + 1)]


def formula_puason(k: int, n: int, p: float) -> float:
    """
    Good when n is very big and lambda between 0.1 and 10
    :param k: number of successful attempts
    :param n: number of attempts
    :param p: successful probability
    :return: probability
    """
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))


def puasson_range(n: int, p: float, start: int) -> float:
    """
     Good when n is very big and lambda between 0.1 and 10
    :param n: number of attempts
    :param p: successful probability
    :param start: point from where start inclusive
    :return: probability of puasson range
    """
    total = 1
    for x in range(start):
        total -= formula_puason(x, n, p)
    return total


def gauss_function(x: float) -> float:
    """
    When gauss function argument bigger than 5, than it equal 0
    :param x: value of searching function
    :return: value of gauss function in the dot x
    """
    return (e ** ((-x ** 2) / 2)) / sqrt(2 * pi)


def local_theorem_of_mavr_laplace(k: int, n: int, p: float) -> float:
    """
    Good for all cases when we search possibility of single variant
    :param k: number of successful attempts
    :param n: number of attempts
    :param p: successful probability
    :return:
    """
    q = 1 - p
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    print('x={}'.format(x))
    return one_divided_by_sqr_of_npq * gauss_function(x)


def laplace_function(x: float) -> float:
    """
    When gauss function argument bigger than 5, than it equal 0.5
    :param x: value of searching function
    :return: value of laplace function in the dot x
    """
    return erf(np.array(x / 2 ** 0.5)) / 2


def reverse_laplace_function(x: float) -> float:
    """

    :param x: value of function in searching point
    :return: argument
    """

    result = float(fsolve(lambda value: laplace_function(value[0]) - x, np.array([1]))[0])
    if result > 5:
        return 5
    elif result < -5:
        return -5
    return result


def integral_theorem_of_mavr_laplace(n: int, k1: int, k2: int, p: float) -> float:
    """

    :param n: number of attempts
    :param k1: number of starting point (inclusive)
    :param k2: number of ending point (exclusive)
    :param p: successful probability
    :return: probability of success
    """
    q = 1 - p
    x1 = (k1 - n * p) / sqrt(n * p * q)
    x2 = (k2 - n * p) / sqrt(n * p * q)
    return laplace_function(x2) - laplace_function(x1)


def three_sigma(n: int, p: float) -> tuple:
    """
    Show variants possible with practical possibility (99.73%)
    :param n: number of attempts
    :param p: successful probability
    :return: return tuple (inclusive, exclusive) of possible variant
    """
    q = 1 - p
    n_p = n * p
    three_sqrt_of_npq = 3 * sqrt(n_p * q)
    return n_p - three_sqrt_of_npq, n_p + three_sqrt_of_npq


def social_mavr_laplace(alfa: float, betta: float) -> int:
    """

    :param alfa: precision
    :param betta: reliability
    :return: how many number of experiments we should conduct
    """
    t_betta = ceil(reverse_laplace_function(betta / 2) * 100) / 100
    return int((t_betta ** 2) / 4 / alfa ** 2) + 1


def social_mavr_laplace_find_biggest_alfa(n: int, betta: float) -> float:
    """

    :param n: number of attempts
    :param betta: reliability
    :return: alfa - precision
    """
    t_betta = ceil(reverse_laplace_function(betta / 2) * 100) / 100
    return sqrt((t_betta ** 2) / 4 / (n - 1))


def social_mavr_laplace_find_biggest_betta(n: int, alfa: float) -> float:
    """

    :param n: number of attempts
    :param alfa: precision
    :return: betta - reliability
    """
    t_betta = sqrt(4 * alfa ** 2 * (n - 1))
    return laplace_function(t_betta) * 2


if __name__ == '__main__':
    print(social_mavr_laplace_find_biggest_betta(6807, 0.01))
    print(social_mavr_laplace_find_biggest_betta(16642, 0.01))
