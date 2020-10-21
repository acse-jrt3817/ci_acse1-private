from functools import lru_cache

__all__ = ['my_sum', 'factorial', 'sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1


def sin(x):
    n = 10
    series = [(x**i)/factorial(i) for i in range(1, 2*n + 1, 2)]
    sign = [1, -1]*n
    sin = sum([series[i]*sign[i] for i in range(n)])
    return sin
