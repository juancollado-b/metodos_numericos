import numpy as np

NEWTON_MAX_ITER = 200


def iteraciones_por_error(a, b, error_decimal):
    ineq = (np.log((b - a) * np.pow(10, error_decimal)) / np.log(2)) - 1
    return int(np.ceil(ineq))



def bisectriz_op(a, b, f, n):
    if n <= 0:
        print("El numero de iteraciones debe ser mayor a 0")
        return None

    f_a = f(a)
    f_b = f(b)
    if f_a * f_b > 0:
        print("El intervalo inicial no cumple con las condiciones del T. Bolzano")
        return None

    for _ in range(n):
        c = (a + b) / 2
        f_c = f(c)

        if f_c == 0:
            return c

        if f_a * f_c < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c

    return (a + b) / 2

# Dado f dos veces derivable y al menos una raiz simple en [a,b]
def newton_raphson(x, f, df, err_newton):
    x_a = x
    # Propongo un numero maximo de iteraciones, que de no cumplir determino no-convergenica
    for i in range(NEWTON_MAX_ITER):
        d_value = df(x_a)
        if d_value == 0:
            print(f"Derivada cero en iteracion {i + 1}. No aplica el metodo.")
            return None

        x_b = x_a - f(x_a) / d_value
        if abs(x_b - x_a) <= err_newton:
            return {"raiz": x_b, "iter": i + 1}
        x_a = x_b

    print(f"No converge para la cantidad de iteraciones definida ({NEWTON_MAX_ITER})")
    return None
