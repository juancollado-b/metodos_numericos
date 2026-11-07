import numpy as np

NEWTON_ERROR = 0.001


def validate_input(a, b, f):
    if (f(a) * f(b)) > 0:
        raise ValueError("El rango es incorrecto")

def condicion_bolzano(a,b,f):
    return f(a) * f(b) < 0


def bisectriz_op(a, b, f, n):
    if not condicion_bolzano(a,b,f):
        print("El intervalo inicial no cumple con las condiciones del T. Bolzano")
        return None

    for _ in range(n):
        c = (a + b) / 2

        if condicion_bolzano(a, c,f): b = c
        elif condicion_bolzano(c, b, f): a=c
        else:
            if f(a) == 0: return a 
            else: return b
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

