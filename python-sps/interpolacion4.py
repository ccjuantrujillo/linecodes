import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Leemos el fichero
data = np.loadtxt("data/data_grafica_cbxa1.txt",dtype=np.double,delimiter="\t",skiprows=0)
(x1,y1) = np.transpose(data)
data = np.loadtxt("data/data_grafica_cbxa2.txt",dtype=np.double,delimiter="\t",skiprows=0)
(x2,y2) = np.transpose(data)
data = np.loadtxt("data/data_grafica_cbxa3.txt",dtype=np.double,delimiter="\t",skiprows=0)
(x3,y3) = np.transpose(data)
data = np.loadtxt("data/data_grafica_cbxa4.txt",dtype=np.double,delimiter="\t",skiprows=0)
(x4,y4) = np.transpose(data)

#Unimos grafica
x = np.concatenate((x1,x2,x3,x4),axis=0)
y = np.concatenate((y1,y2,y3,y4),axis=0)
f1  = interp1d(x1,y1)
f2  = interp1d(x2,y2)
f3  = interp1d(x3,y3)

#Interpolacion cubica
xp1 = np.arange(1,30,1)
xp2 = np.linspace(0,30,num=60,endpoint=True)
yp1 = f1(xp1)
yp2 = f2(xp2)
xp = np.concatenate((xp1,xp2),axis=0)
yp = np.concatenate((yp1,yp2),axis=0)

#Plot data
plt.ylabel("x")
plt.xlabel("y")
plt.plot(x,y,'ko',label='Data')
plt.plot(xp,yp,'-')
plt.legend(loc='best')
plt.show()