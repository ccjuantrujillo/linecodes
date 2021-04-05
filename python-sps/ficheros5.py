import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("interpolacion_data_polar.txt",dtype=np.double,delimiter="\t",skiprows=0)
(theta,radio) = np.transpose(data)

#Plot data polar
ax = plt.subplot(111,polar=True)
ax.plot(theta*np.pi/180,radio)
plt.grid()
plt.show()