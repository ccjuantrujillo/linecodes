import numpy as np
import matplotlib.pyplot as plt
xep  = np.linspace(-np.pi,np.pi,21)
yexp = np.sin(xep)

#Interpolación
x=np.linspace(-np.pi,np.pi,10)
y=np.interp(x,xep,yexp)

plt.plot(xep,yexp)
plt.plot(x,y,'o')
plt.show()