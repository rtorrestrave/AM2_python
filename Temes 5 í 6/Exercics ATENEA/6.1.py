'''
P6.1 Sigui el problema de valor inicial
y′ = t^2 / (y − 1)  1 ≤ t ≤ 2
y(1) = 3
(a) Apliqueu el mètode d’Euler amb passos h = 1/4 h = 1/8 i h = 1/16
per aproximar el valor de y(2).
(b) Compareu els resultats amb la solució exacta, sabent que la solució
analítica és y(t) = 1 + root(2/3*(t^3 + 5).
(c) Feu una gràfica amb les tres aproximacions i la solució exacta.
'''

import numpy as np
import matplotlib.pyplot as plt

def euler(f, t0, tf, y0, h):
    N = int(round((tf-t0)/h)) # NUMERO DE PASOS
    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0 #CONDICIÓ
    y[0] = y0 #CONDICIÓ INICIAL

    for i in range(0,N):
        y[i+1]= y[i] + h*f(t[i],y[i])
        t[i+1] = t[i] + h

    return t, y

def f(t,y):
        return t**2/(y-1)
def y_exacte(t):
        return 1+np.sqrt((2/3)*(t**3+5))

# a)
t0 = 1
tf = 2
y0 = 3

print(f'Valor exacte: y(2) = {y_exacte(2)}')

for h in [1/4, 1/8, 1/16]:
    t, y = euler(f, t0, tf, y0, h)
    N = len(t)-1
    error = abs(y_exacte(2)-y[N])
    print(f'h={h}, y_aprox(2) = {y[N]}, error={error}')

# c)
for h in [1/4, 1/8, 1/16]:
    t, y = euler(f, t0, tf, y0, h)
    plt.plot(t, y, '--', label = f'Euler, h={h}')

plt.plot(t, y_exacte(t), 'k-', label='Exacte')
plt.legend()
plt.show()