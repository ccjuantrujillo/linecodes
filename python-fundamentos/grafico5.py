from pylab import *
lista1 = [11,2,3,15,8,13,21,34]
plt.plot(lista1)
plt.xlabel("abscisa")
plt.ylabel("ordenada")
plt.ioff()
lista2 = [2,3,4,2,3,6,4,10]
plt.plot(lista2)
plt.ion()
plt.plot(lista2)
plt.show()
plt.ioff()