#Convierte puntos de coordenadas rectangulares a polares
#Y hace una interpolación lineal
import numpy as np
import matplotlib.pyplot as plt

#Leemos el fichero
data = np.loadtxt("data/data_antena.txt",dtype=np.double,delimiter="\t",skiprows=0)

#Convertimos a polares
datapolar = np.ones((np.size(data,0),2))
datapolar[:,0] = np.arctan2(data[:,1],data[:,0])*180/np.pi
datapolar[:,1] = np.sqrt(np.power(data[:,0],2) + np.power(data[:,1],2))
for fila in datapolar:
    if (fila[0] < 0):
        fila[0] = fila[0] + 360
datapolar_sorted = sorted(datapolar.tolist())

#Extraemos coordenadas
(th,r) = np.transpose(datapolar_sorted)

#Interpolación de datos y graficamos
thp = np.arange(0,360,1)
rp  = np.interp(thp,th,r)
#plt.plot(thp,rp,'ro')
#plt.show()

#Guardamos en un fichero
p = np.array([thp.tolist(),rp.tolist()])
p = np.transpose(p)
np.savetxt("data/data_antena_polar.txt",p,delimiter="\t")

#Plot data
fig = plt.figure()
ax  = fig.add_subplot(111,projection="polar")
ax.plot(thp*np.pi/180,rp)
plt.show()