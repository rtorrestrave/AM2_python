'''
Sigui el problema de valor inicial:
y′ − y = t, 0 ≤ t ≤ 3
y(0) = 1

(a) Utilitzeu el mètode d’Euler millorat (Heun) donat per: y i+1 = yi +
h/2 * (f(ti, yi) + f(ti + h, yi + hf(ti, yi))
per trobar el valor y(3), amb passos h = 1/2, h = 1/4 i h = 1/8.
(b) Compareu els resultats amb la solució exacta, y(3), sabent que la
solució analítica és y(t) = 2e^t − t − 1.
(c) Feu una gràfica amb les tres aproximacions i la solució exacta.
'''

import numpy as np
import matplotlib.pyplot as plt

def RK2_heun (f, t0, tf, y0, h ):
    N = int(round((tf - t0)/h))
    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0
    y[0] = y0

    for i in range(0,N):
        k1 = f(t[i], y[i])
        k2 = f(t[i] +h , y[i]+h*k1)
        y[i+1] = y[i]+h*((k1+k2)/2)
        t[i+1] = t[i]+h

    return t, y

def f(t,y):
    return t+y
def y_exacte(t):
    return 2*(np.exp(t)) - t - 1

# a)
t0 = 0
tf = 3
y0 = 1

for h in [1/2, 1/4, 1/8]:
    t, y = RK2_heun(f, t0, tf, y0, h)
    N = len(t)-1
    error = abs(y_exacte(3)-y[N])
    print(f' h = {h}, y_aprox(2) = {y[N]} error = {error}')

for h in [1/2, 1/4, 1/8]:
    t, y = RK2_heun(f, t0, tf, y0, h)
    plt.plot(t, y, '--')

plt.plot(t,y_exacte(t), 'k-')
plt.show()
