from math import factorial, e, sqrt, pi
from scipy.special import erf


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)


def theorem_bernuli(k: int, n: int, p: float, q: float) -> float:
    '''
    :param k: number of successful attempt
    :param n: number of attempts
    :param p: successful probability
    :param q: unsuccessful attempt
    :return: result of theorem bernuli
    '''
    return combination(k, n) * (p ** k) * (q ** (n - k))


# write puason from to infinity
def formula_puason(k: int, n: int, p: float) -> float:
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))


def gauss_function(x: float) -> float:
    return (e ** ((-x ** 2) / 2)) / sqrt(2 * pi)


# todo q get from p
def local_theorem_of_mavr_laplas(k: int, n: int, p: float, q: float) -> float:
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    print('x={}'.format(x))
    return one_divided_by_sqr_of_npq * gauss_function(x)


def laplassFunction(x: float) -> float:
    return erf(x / 2 ** 0.5) / 2


def integral_theorem_of_mavr_laplas(n: int, k1: int, k2: int, p: float) -> float:
    q = 1 - p
    x1 = (k1 - n * p) / sqrt(n * p * q)
    x2 = (k2 - n * p) / sqrt(n * p * q)
    return laplassFunction(x2) - laplassFunction(x1)

print(integral_theorem_of_mavr_laplas(10_000, 4_850, 5_149, 0.5))