import matplotlib.pyplot as plt
import numpy as np

# Dibuixar la grafica de x^2 en l'interval [0,4]

x = np.linspace (0, 6, 100)
y = np.sin(x)

plt.plot (x, y)
plt.show()

####################################################################3
import matplotlib.pyplot as plt
import numpy as np
 x = np.linspace (0, 4, 100)
 y = x**2

 plt.plot (x, y, '--', label = '$y=x^2$')
 plt.xlabel('x')
 plt.ylabel('y')
 plt.title('Grafica de $y=x^2$ en $[0,4]$')
 plt.grid(True)
 plt.legend()
 plt.show()