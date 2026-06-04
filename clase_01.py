"""
CLASE 01 - Metodos numericos
"""
import matplotlib.pyplot as plt
import numpy

pi_cos = numpy.cos(numpy.pi)
pi_sen = numpy.sin(numpy.pi / 2)

print(f"Cos pi = {pi_cos} \n Sin pi/2 = {pi_sen}")

exp = numpy.exp(2) # e^2

log = numpy.log(3)

log_10 = numpy.log10(40)

f = lambda x: x ** 2 - 2*numpy.cos(x)
x = numpy.arange(-1, 8) # desde -1 a 7
print(f"Arrange -> {x}")

y = f(x)
print(f"Function f: {y}")


# plt.plot(x,  y)
# plt.show()


# Print triangle with matplot
xt = [1, 3, 2, 1]
yt = [1, 2, 4, 1]

plt.plot(xt,  yt)
plt.show()
