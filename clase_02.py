import time
import numpy as np


def sumatoria(iter):
    accum = 0
    for i in range(1, iter + 1):
        accum += 1 / (i * i)
    return accum


def sumatoria_np(iter):
    n = np.arange(1, iter + 1)
    return np.sum(1 / (n*n))


start = time.time()
result = sumatoria(5000000)
end = time.time()
print(f"Result: {result}")

print((end - start) * 1e3, "ms")

print("complex")
start_c = time.time()
result_c = sumatoria_np(5000000)
end_c = time.time()
print(f"Result: {result_c}")

print((end_c - start_c) * 1e3, "ms")
