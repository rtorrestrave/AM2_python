'''
     El fitxer temps-posicio.txt conté dues columnes de dades, corresponents a les mesures
    de temps i posició d’un sensor. Suposarem que les mesures de temps són equiespaiades.
    (a) Llegeix les mesures i dibuixa la gràfica de la funció posició.
    (b) Utilitza les aproximacions de la derivada i de la derivada segona:

    ˜f′(t) = f(t) − f(t − h) / h
    ˜f′′(t) = f(t + h) − 2f(t) + f(t − h) / h^2

    per dibuixar les funcions velocitat i acceleració.
    (c) Utilitza l’aproximació de la derivada

    ˜f′(t) = −f(t + 2h) + 8f(t + h) − 8f(t − h) + f(t − 2h) / 12h

    per calcular el valor aproximat de la velocitat en l’instant t = 400.

    (d) Si el temps est`a mesurat en milisegons i la posició en centímetres, calcula les velocitats
    mitjanes en km/h en la primera meitat de l’interval i en la segona meitat de l’interval.
'''

######################### A #############################
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
f=open('temps-posicio.txt', 'r')
text=f.readline()
while text:
    trozos = text.split()
    x.append(float(trozos[0]))
    y.append(float(trozos[1]))
    text = f.readline()
plt.plot(x,y)
plt.show()

f.close()
######################### B #############################
f=open('temps-posicio.txt', 'r')

lin1 = f.readline()
lin2 = f.readline()

a = 0
b = 799
h = int(lin2) - int(lin1)

nB = int((b-a)/h)
xB = np.linspace(a,b,nB+1)
der = []

######################### B #############################
'''
    Per trobar t=400, no pots posar temps[400], has de trobar a quina posicio esta el t=400
    Això es pot fer amb:
    o una busqueda
    
    ó
    
    saps que t[0] + h * i = 400
        ==> i = (400-t[0])
'''
