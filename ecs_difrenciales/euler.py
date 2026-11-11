import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    xs = [x]
    ys = [y]

    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h

        xs.append(x)
        ys.append(y)

    return xs, ys

# Ejemplo: y' = x + y
def f(x, y):
    return x + y


points = euler(f, 0, 1, 0.01, 1000)

# for x, y in results:
#     print(f"x = {x:.2f}, y = {y:.5f}")


# Solución analítica
x_exact = np.linspace(0, 10, 1000)
y_exact = 2 * np.exp(x_exact) - x_exact - 1

plt.plot(*points, 'o--', label='Euler')
plt.plot(x_exact, y_exact, label='Solución exacta')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler vs. solución exacta')

plt.grid(True)
plt.legend()
plt.show()

plt.show()