import matplotlib.pyplot as plt
from numpy import *

x,y = mgrid[-2:2:1000j,-2:2:1000j]
a = (sqrt(x**2+y**2)<1)
plt.imshow(a,cmap=plt.cm.Greys)
plt.show()