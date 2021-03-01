#codigo para generar el triangulo con la union de puntos de manera aleatoria

import random
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np


#print(dado)

#triangulo
#lado1
pointl1 = [500, 750]
pointl2 = [1500, 2500]
#lado2
pointl1_2 = [2500, 750]
#base
pointb1 = [500, 750]
pointb2 = [2500, 750]
x = [pointb1[0], pointb2[0], pointl1[0], pointl2[0], pointl1_2[0]]
y = [pointb1[1], pointb2[1], pointl1[1], pointl2[1], pointl1_2[1]]

plt.plot(x, y)
#eligimos un punto
p = [1800, 1600]
plt.plot(p[0], p[1], marker=".", color="black")


for i in range(10000):
    #hacemos un vector
    dado = random.randrange(0, 3) #dado de 3 caras
    puntosx = [500, 1500, 2500]
    puntosy = [750, 2500, 750]
    nx = [p[0], puntosx[dado]]
    ny = [p[1], puntosy[dado]]
    #plt.plot(nx, ny, color="white")
    #calculamos la mitad del vector, el punto medio
    m = [(p[0]+puntosx[dado])/2,(p[1]+puntosy[dado])/2]
    plt.plot(m[0], m[1], marker=".", color="green")
    
    #guardamos nuevo punto con el punto medio calculado
    p = m


plt.show()

