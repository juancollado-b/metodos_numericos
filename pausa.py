import os
os.system('cls' if os.name == 'nt' else 'clear')
import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,10,0.1)

f= lambda x: np.sin(x)

plt.figure(1) # Crear una ventana donde graficar
plt.grid() # Grilla del grafico
#plt.legend() # Leyenda de los graficos
plt.axhline(0, color='black', linewidth=0.5)#Dibuja eje x
plt.axvline(0, color='black', linewidth=0.5)#Dibuja eje y
plt.axis([0,10,-1.1,1.1])

for i in np.arange(0,10,0.1):
    plt.plot(i,f(i), label = "Funcion Seno", marker=".",markersize=10, linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
# Identificar los puntos, la forma de lina, el color
    plt.xlabel("t") # Nombre del eje X
    plt.ylabel("f(t)") # Nombre del eje Y
    plt.title("Funciones Trigonométricas") # Titulo del grafico
    plt.pause(0.005)
plt.show()
