import numpy as np

expon=lambda x: np.exp(x)
cuadr = lambda x: np.pow(x, 2)
print("cuad", cuadr(2))
def riemman(a,b, N, f):
    h = (b-a)/N
    puntos_medios = np.arange(a+h/2, b, h)
    y = f(puntos_medios)
    integ = sum(y) * h
    return integ


def trapecios_c(a,b, n, f):
    h = (b-a)/n
    ptos = np.arange(a+h, b, h)
    y = f(ptos)
    sum_ev = np.sum(y)
    return (h/2)*(f(a)+f(b)+2*sum_ev)

def simpson_c(a,b,n, f):
    if n % 2 != 0:
        return False
    
    h = (b-a)/n
    pares = f(np.arange(a + 2*h, b, 2*h))
    impares = f(np.arange(a + h, b, 2*h))

    return (h/3)*(f(a)+f(b)+2*np.sum(pares)+4*np.sum(impares))


result_r = riemman(0,1,34, expon)
result_t = trapecios_c(0,2, 10000, cuadr)
result_s = simpson_c(0, 2, 10000, cuadr)
print("RESULT", result_r)
print("RESULT TRAPECIO", result_t)
print("RESULT SIMPSON", result_s)