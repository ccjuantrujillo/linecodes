from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,num=11,endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x,y,kind='cubic')

xnew = np.linspace(0,10,num=40,endpoint=True)
ynew = f(xnew)

plt.plot(x,y,'o',xnew,ynew,'-')
plt.legend(['data','cubic'],loc='best')
plt.show()