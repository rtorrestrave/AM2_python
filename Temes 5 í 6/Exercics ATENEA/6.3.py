'''
P6.3 El problema de valor inicial
y′ = (y^2 + y) / t per 1 ≤ t ≤ 3
y(1) = −2
té solució analítica y(t) = 2t / (1 − 2t)

En els dos apartats següents, els mètodes numèrics han d’estar dins d’una funció
(a) En l’interval [1, 3] aproximeu la solució de l’equació pel mètode d’Euler amb passos
h = 1/4, h = 1/8 i h = 1/16 .
Feu la representació gràfica de les aproximacions trobades i de la solució analítica,
en una sola finestra, i comproveu les diferències.
(b) Calculeu, amb cadascun dels mètodes següents, el valor de l’aproximació en t = 3.
Calculeu l’error en cadascuna de les aproximacions.
• Mètode d’Euler amb h = 1/8
• Mètode de Runge-Kutta de punt mig amb h = 1/8.
• Mètode de Runge-Kutta d’ordre 3 amb h = 1/8.
'''

import numpy as np
import matplotlib.pyplot as plt

def euler (f, t0, tf, y0, h):
    N = int(round((tf-t0)/h))
    t = np.zeros(N+1)
    y = np.zeros(N+1)

    t[0] = t0
    y[0] = y0

    for i in range(0,N):
        y[i+1] = y[i] + h*f(t[i],y[i])
        t[i+1] = t[i] + h

    return t,y

def f(t,y):
    return (y**2+y)/t
def y_bona(var):
    return 2*var/(1-2*var)

# a)
t0 = 1
tf = 3
y0 = -2


for h in [1/4, 1/8, 1/16]:
    t, y = euler(f, t0, tf, y0, h)
    N = len(t)-1
    plt.plot(t,y, '-', label=f'h = {h}')
plt.plot(t,y_bona(t), 'k-', label = "bona")
plt.legend()
plt.show()
# b)
asdf = euler(f, t0, 3, y0, 1/8)
fdsa = asdf[1]
print(fdsa[-1])
