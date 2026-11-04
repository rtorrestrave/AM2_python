# Carreguem el fitxer
import numpy as np

A = np.loadtxt('dades_regressio.txt')
print(f'Mida: {A.shape}')

t = A[:,0]
x = A[:,1]
print(f't={t}')
print(f'x={x}')
print(f'Numero de punts: {len(t)}')