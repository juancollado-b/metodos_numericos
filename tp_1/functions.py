import numpy as np
import matplotlib.pyplot as plt

NEWTON_MAX_ITER = 200


def bisectriz(a, b, f, n):
    if (f(a) * f(b)) > 0:
        print("El intervalo elegido no cumple con bolzano.")
        return None

    for _ in range(n):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return {"a": a, "b": b, "resultado": (a + b) / 2}


def newton_raphson(x, f, df, err_newton):
    x_a = x
    # Propongo un numero maximo de iteraciones, que de no cumplir determino no-convergenica
    for i in range(NEWTON_MAX_ITER):
        d_value = df(x_a)
        if d_value == 0:
            print("Derivada cero. No aplica metodo.")
            return None

        x_b = x_a - f(x_a)/d_value
        if abs(x_b - x_a) <= err_newton:
            return {"raiz": x_b, "iter": i+1}
        x_a = x_b

    print("No converge")

def aproximacion_raiz(f, df, n_biseccion, int_biseccion, err_newton):
    res_bisectriz = bisectriz(int_biseccion["a"], int_biseccion["b"], f, n_biseccion)
    if not res_bisectriz: return None

    res_newton = newton_raphson(res_bisectriz["resultado"], f, df, err_newton)
    return {"intervalo_bisec": (res_bisectriz["a"], res_bisectriz["b"]), **res_newton}

def graficar_funcion(f, raices=(), intervalo=(-5, 10), puntos=200):
    x = np.linspace(intervalo[0], intervalo[1], puntos)
    y = f(x)

    plt.figure()

    # Curva de la función
    plt.plot(x, y, marker='o', linestyle='-', label='f(x)')

    # Eje x
    plt.axhline(0)

    if len(raices):
        for raiz in raices:
            # Línea vertical roja punteada
            plt.axvline(raiz, linestyle='--', color='red', label=f'Raíz ≈ {raiz:.4f}')

            # Punto rojo en la raíz
            plt.scatter(raiz, f(raiz), color='red', zorder=3)

    plt.title("Aproximacion raices")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()

    plt.show()