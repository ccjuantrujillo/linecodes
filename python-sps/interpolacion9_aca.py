#Cambia de ejes coordenadas polares en el formato RadioMobile
import numpy as np
import matplotlib.pyplot as plt

#Leemos el fichero
data = np.loadtxt("data/data_antena_polar.txt",dtype=np.double,delimiter="\t",skiprows=0)

##Rotamos el sistema de coordenadas
data[:,1] = data[:,1] - max(data[:,1])#Radio en decibel (db)
data[:,0] = 360 - data[:,0]
#for fila in data:
#    if (fila[0] > 360):
#        fila[0] = fila[0] - 360
data = sorted(data.tolist())

#Extraemos coordenadas
(th,r) = np.transpose(data)

#Guardamos en un fichero
p = np.array([th.tolist(),r.tolist()])
p = np.transpose(p)
np.savetxt("data/data_antena_polar_rotado.txt",p,delimiter="\t")

#Plot data th vs r
plt.plot(th,r,'r.')
plt.show()

#Plot data
fig = plt.figure()
ax  = fig.add_subplot(111,projection="polar")
ax.plot(th*np.pi/180,r)
plt.show()