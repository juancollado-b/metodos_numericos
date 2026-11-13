import matplotlib.pyplot as plt
import numpy as np


def grafico(a, b, f, pasos=1000):
    xs = np.linspace(a, b, pasos)
    ys = f(xs)

    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()
    plt.show()
