import numpy as np
import matplotlib.pyplot as plt

#Obtenemos r y th
#theta = np.linspace(0,2*np.pi)
#r = 5 + 50*theta
data = np.loadtxt("interpolacion_data.txt",dtype=np.double,delimiter="\t",skiprows=0)
(th,r) = np.transpose(data)

fig = plt.figure()
ax  = fig.add_subplot(111,projection="polar")
ax.plot(th*np.pi/180,r)

plt.show()