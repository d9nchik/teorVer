from math import factorial, e, sqrt, pi


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)


def theorem_bernuli(k: int, n: int, p: float, q: float) -> float:
    return combination(k, n) * (p ** k) * (q ** (n - k))


def formula_puason(k: int, n: int, p: float) -> float:
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))


def gauss_function(x: float) -> float:
    return (e ** ((-x ** 2) / 2)) / sqrt(2 * pi)


def local_theorem_of_mavr_laplas(k: int, n: int, p: float, q: float) -> float:
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    return one_divided_by_sqr_of_npq * gauss_function(x)


print(local_theorem_of_mavr_laplas(5000, 10000, 0.5, 0.5))
