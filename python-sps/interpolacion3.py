import numpy as np
import matplotlib.pyplot as plt

xm = np.array([-238.9425,-202.4301,-173.3452,-84.7480,35.5634,134.2995,166.6695,178.4842,148.3249,186.9665,206.7586])
ym = np.array([-32.0109,-77.4280,-138.9777,-194.3612,-201.7143,-153.6368,-111.9458,-96.7291,-131.5526,-81.6703,-24.2586])

#spline cubic
from gekko import GEKKO
m = GEKKO()
m.x = m.Param(value=np.linspace(-240,210))
m.y = m.Var()
m.cspline(m.x,m.y,xm,ym)
m.options.IMODE = 2
m.solve(disp=False)

#Guardamos en ficherokelly
p = np.array([m.x.value,m.y.value])
p = np.transpose(p)
np.savetxt("interpolacion_data.txt",p,delimiter="\t")
r  = np.sqrt(np.power(m.x,2) + np.power(m.y,2))
th = np.arctan2(m.y, m.x) * 180 / np.pi
p = np.array([th.tolist(),r.tolist()])
p = np.transpose(p)
np.savetxt("interpolacion_data_polar.txt",p,delimiter="\t")

#plot data
plt.ylabel("x")
plt.xlabel("y")
plt.plot(xm,ym,'ko',label='Data')
plt.plot(m.x,m.y,'r--',label='Cubic spline')
plt.legend(loc='best')
plt.show()