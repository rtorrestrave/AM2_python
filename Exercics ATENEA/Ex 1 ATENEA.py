'''
P5.1 Sigui f(x) = e^x i, per tant, f′(x) = e^x. Fes un programa que aproximi f′(x) en l’interval
[0, 2], utilitzant l’aproximació de la derivada per diferències endavant. Utilitza diferents
valors del pas i representa en la mateixa gràfica la funció i la seva aproximació. Comprova
què passa si prens un pas molt gran, i si prens un pas molt petit. Fes la prova amb altres
funcions.
'''

import math
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2
h = 0.25 #Pas

n = int((b-a)/h) # eL numero d'espais, de salts que es fa
x = np.linspace(a,b,n+1)
der = []

for i in range(len(x)):
    p = (np.exp(x[i]+h)-np.exp(x[i]))/h
    der.append(p)

print(x)

xaxis = np.linspace(0,2,n)
plt.plot(x, der)
plt.plot(x,np.exp(x))
plt.show()



