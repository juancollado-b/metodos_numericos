import numpy as np

NEWTON_ERROR = 0.001


def validate_input(a, b, f):
    if (f(a) * f(b)) > 0:
        raise ValueError("El rango es incorrecto")


def bisectriz_op(a, b, f, n):
    validate_input(a, b, f)

    for i in np.arange(n):
        c = (a + b) / 2
        if not (f(a) * f(c) < 0):
            a = c
        elif f(b) * f(c) > 0:
            b = c
    return c


def newton_raphson(x, f, df):
    x_a = x
    while True:
        derivate_value = df(x_a)
        if derivate_value == 0: break
        x_b = x_a - (f(x_a) / derivate_value)
        if abs(x_b - x_a) <= NEWTON_ERROR: break
        x_a = x_b

    return x_a

