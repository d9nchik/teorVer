import numpy as np
from math import factorial, e, sqrt, pi, ceil
from scipy.special import erf
from scipy.optimize import fsolve


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
def local_theorem_of_mavr_laplace(k: int, n: int, p: float, q: float) -> float:
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    print('x={}'.format(x))
    return one_divided_by_sqr_of_npq * gauss_function(x)


def laplace_function(x: float) -> float:
    return erf(x / 2 ** 0.5) / 2


def reverse_laplace_function(x: float) -> float:
    return float(fsolve(lambda value: laplace_function(value) - x, np.ndarray([1]))[0])


def integral_theorem_of_mavr_laplace(n: int, k1: int, k2: int, p: float) -> float:
    q = 1 - p
    x1 = (k1 - n * p) / sqrt(n * p * q)
    x2 = (k2 - n * p) / sqrt(n * p * q)
    return laplace_function(x2) - laplace_function(x1)


def social_mavr_laplace(alfa: float, betta: float):
    t_betta = ceil(reverse_laplace_function(betta / 2) * 100) / 100
    print(t_betta)
    return int((t_betta ** 2) / 4 / alfa ** 2) + 1


print(social_mavr_laplace(0.01, 0.99))
