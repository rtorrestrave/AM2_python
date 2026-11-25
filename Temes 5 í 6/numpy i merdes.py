import numpy as np
import math

n = 0
k = 5

while n < k:
    n = n + 1
    print(f'n={n}')
print(f'Fuera n={n}')


for i in range(2,10,2): #de 2 a 10 de 2 en 2
    print(i)
for i in range (5,2): #això no treu res pq el pas es 1
    print(i)
for i in range(5,2,-1):
    print(i)

#################### crear funcions ####################
def funcio(a):
    #.....
    return resultat
a = funcio(a)

################### numpy #####################
import numpy as np
# creem un array
x = np.linspace(0,10,11) ## va de 0 a 10 entre 11 numeros, evently spaced
print(x)
y= x**2
print(y)

a = range(0,10)
print(list(a))

# Creem un array de zeros
a = np.zeros(15)
print(a)

# Creen un array d'uns
b = np.ones(15)
print(b)

############# np.arange
c = np.arange(5)
print(f'c={c}')

d = np.arange(0,1,0.25) #(inici, final, pas)
print(f'd={d}')

e = np.linspace(0,1,5) # (inici, final, numero de punts
print(f'e={e}')

# Cuidado amb el "redondeo" en np.arange
p = np.arange(1,1.3, 0.1)
print(f'p={p}')