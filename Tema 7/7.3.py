import numpy as np

Dx = 1/3
Dy = 1/3
x0 = 1
xf = 2
y0 = 0
yf = 1

n = int((xf-x0)/Dx)
m = int((yf-y0)/Dy)

x = np.linspace(x0,xf,n+1)
y = np.linspace(y0,yf,n+1)

W = np.zeros((n+1,n+1))
print(W)

for i in range(n+1):
    W[i][0] = 2*np.log(x[i])
    W[i][m] = 2 * np.log(x[i])
