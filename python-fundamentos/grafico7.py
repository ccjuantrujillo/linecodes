from pylab import *
paises = ("Alemania","España","Francia","Portugal")
posicion_y = np.arange(len(paises))
unidades = (342,321,192,402)
plt.barh(posicion_y,unidades,align="center")
plt.yticks(posicion_y,paises)
plt.xlabel("Unidades vendidas")
plt.title("Ventas en Europa")
plt.show()