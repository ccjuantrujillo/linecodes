import numpy as np
import matplotlib.pyplot as plt

datos = np.arange(0,360)
datos = np.radians(datos)
datos = np.cos(datos)

plt.plot(datos,"b--")
plt._show()
plt.savefig("coseno.png")