import numpy as np
import matplotlib.pyplot as plt
from matplotlib import axes

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

        x_b = x_a - f(x_a) / d_value
        if abs(x_b - x_a) <= err_newton:
            return {"raiz": x_b, "iter": i + 1}
        x_a = x_b

    print("No converge")


def aproximacion_raiz(f, df, n_biseccion, int_biseccion, err_newton):
    res_bisectriz = bisectriz(int_biseccion["a"], int_biseccion["b"], f, n_biseccion)
    if not res_bisectriz:
        return None

    res_newton = newton_raphson(res_bisectriz["resultado"], f, df, err_newton)
    return {"intervalo_bisec": (res_bisectriz["a"], res_bisectriz["b"]), **res_newton}


def _xscale_raices(ax: axes.Axes, f, raices=[], intervalo=(-5, 10), salto=1) -> None:
    """
    (FUNCION EXTRA) Tiene como objetivo configurar el eje X del plot
    Toma el intervalo a dibujar y un salto.
    Recorre el intervalo y coloca la raiz donde corresponse en el eje X y traza una linea horizontal
    """
    range_intervalo = range(intervalo[0], intervalo[1] + 1, salto)
    sorted_raices = sorted(raices)
    if not len(raices):
        ax.set_xticks(range_intervalo)
        return

    i_raices = 0
    xticks = []
    raices_placed = []
    for i, v in enumerate(range_intervalo):
        raiz = sorted_raices[i_raices]
        difference = abs(raiz - v)
        if difference < salto / 2:
            xticks.append(raiz)
            ax.scatter(raiz, f(raiz), color="red", zorder=3, label=f"Raíz ≈ {raiz:.4f}")
            raices_placed.append(i)
            i_raices += 1
            if len(raices) < i_raices + 1:
                xticks.extend(range_intervalo[i + 1 :])
                break
        else:
            xticks.append(v)

    ticks = ax.set_xticks(xticks)
    for raiz in raices_placed:
        ticks[raiz].label1.set_color("red")
        ticks[raiz].tick1line.set_markeredgecolor("red")
        ticks[raiz].gridline.set(
            visible=True, linestyle=":", linewidth=1.5, color="red"
        )


def graficar_funcion(f, raices=(), intervalo=(-5, 10), puntos=200, x_salto=1):
    x = np.linspace(intervalo[0], intervalo[1], puntos)
    y = f(x)

    fig, ax = plt.subplots()
    ax.axhline(color="gray", linewidth=0.5)
    ax.axvline(color="gray", linewidth=0.5)
    ax.plot(x, y, linestyle="-", color="black", label="f(x)")
    _xscale_raices(ax, f, raices, intervalo, x_salto)

    ax.set_title("Aproximacion raices")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()

    plt.show()
