import numpy as np
import matplotlib.pyplot as plt

datos = np.arange(0,360)
datos = np.radians(datos)
datos = np.sin(datos)

plt.plot(datos,"b--")
plt.show()