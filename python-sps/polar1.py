import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('default')

theta = np.linspace(0,2.0*np.pi,2001)
curva = np.cos(0.5*np.pi*np.cos(theta))/np.sin(theta)
ax1=plt.subplot(111,polar=True)
ax1.plot(theta,curva)
plt.grid()
plt.show()