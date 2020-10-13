import numpy as np
from math import factorial, e, sqrt, pi, ceil, floor
from scipy.special import erf
from scipy.optimize import fsolve


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)


def theorem_bernuli(k: int, n: int, p: float) -> float:
    '''
    :param k: number of successful attempt
    :param n: number of attempts
    :param p: successful probability
    :return: probability
    '''
    q = 1 - p
    return combination(k, n) * (p ** k) * (q ** (n - k))


def most_possible_success_variants(n: int, p: float):
    '''
    :param n: number of attempts
    :param p: successful probability
    :return: most possible success variants
    '''
    q = 1 - p
    first = ceil(n * p - q)
    second = floor(n * p + p)
    return [x for x in range(first, second + 1)]


# write puason from to infinity
def formula_puason(k: int, n: int, p: float) -> float:
    '''
    Good when n is very big and lambda between 0.1 and 10
    :param k: number of successful attempts
    :param n: number of attempts
    :param p: successful probability
    :return: probability
    '''
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))


def puasson_range(n: int, p: float, start: int) -> float:
    total = 1
    for x in range(start):
        total -= formula_puason(x, n, p)
    return total


def gauss_function(x: float) -> float:
    return (e ** ((-x ** 2) / 2)) / sqrt(2 * pi)


def local_theorem_of_mavr_laplace(k: int, n: int, p: float) -> float:
    q = 1 - p
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    print('x={}'.format(x))
    return one_divided_by_sqr_of_npq * gauss_function(x)


def laplace_function(x: float) -> float:
    return erf(x / 2 ** 0.5) / 2


def reverse_laplace_function(x: float) -> float:
    return float(fsolve(lambda value: laplace_function(value[0]) - x, np.eye(1))[0])


def integral_theorem_of_mavr_laplace(n: int, k1: int, k2: int, p: float) -> float:
    q = 1 - p
    x1 = (k1 - n * p) / sqrt(n * p * q)
    x2 = (k2 - n * p) / sqrt(n * p * q)
    return laplace_function(x2) - laplace_function(x1)


def social_mavr_laplace(alfa: float, betta: float):
    t_betta = ceil(reverse_laplace_function(betta / 2) * 100) / 100
    print(t_betta)
    return int((t_betta ** 2) / 4 / alfa ** 2) + 1


if __name__ == '__main__':
    print(integral_theorem_of_mavr_laplace(3600, 1959, 3601, 0.5))
