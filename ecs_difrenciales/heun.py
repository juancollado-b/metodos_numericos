import matplotlib.pyplot as plt
import numpy as np


# Método de Heun
def heun(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    for _ in range(n):
        x = xs[-1]
        y = ys[-1]

        k1 = f(x, y)
        y_1 = y + h * k1
        k2 = f(x + h, y_1)

        k_promedio = (k1 + k2) / 2
        y_next = y + h * k_promedio

        xs.append(x + h)
        ys.append(y_next)

    return xs, ys


# Ejemplo: y' = x + y
def f(x, y):
    return x + y


points = heun(f, 0, 1, 0.1, 100)

# Solución analítica
x_exact = np.linspace(0, 10, 100)
y_exact = 2 * np.exp(x_exact) - x_exact - 1

plt.plot(*points, "o--", label="Heun")
plt.plot(x_exact, y_exact, label="Solución exacta")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Método de Heun vs. solución exacta")

plt.grid(True)
plt.legend()
plt.show()

plt.show()
