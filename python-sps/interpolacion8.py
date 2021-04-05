import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([0.1,0.2,0.3,0.5,1.0,0.9])

#interpolación
xp = np.linspace(0,5,30)
yp = np.interp(xp,x,y)

#plot data
plt.ylabel("x")
plt.xlabel("y")
plt.plot(x,y,'ko',label='Data')
plt.plot(xp,yp,'r')
plt.legend(loc='best')
plt.show()

