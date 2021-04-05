import numpy as np
import matplotlib.pyplot as plt

xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,1.0,0.9])

#spline cubic
from gekko import GEKKO
m = GEKKO()
m.x = m.Param(value=np.linspace(-1,8))
m.y = m.Var()
m.cspline(m.x,m.y,xm,ym)
m.options.IMODE = 2
m.solve(disp=False)

#plot data
plt.ylabel("x")
plt.xlabel("y")
plt.plot(xm,ym,'ko',label='Data')
plt.plot(m.x,m.y,'r--',label='Cubic spline')
plt.legend(loc='best')
plt.show()

