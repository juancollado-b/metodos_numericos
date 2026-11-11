import matplotlib.pyplot as plt
import numpy as np

# Runge-Kutta de cuarto orden
def rk4(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    for _ in range(n):
        x = xs[-1]
        y = ys[-1]

        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)

        y_next = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        xs.append(x + h)
        ys.append(y_next)

    return xs, ys


# Ejemplo: y' = x + y
def f(x, y):
    return x + y

points = rk4(f, 0, 1, 0.1, 100)

# Solución analítica
x_exact = np.linspace(0, 10, 100)
y_exact = 2 * np.exp(x_exact) - x_exact - 1

plt.plot(*points, 'o--', label='Euler Modificado')
plt.plot(x_exact, y_exact, label='Solución exacta')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler Modificado vs. solución exacta')

plt.grid(True)
plt.legend()
plt.show()

plt.show()