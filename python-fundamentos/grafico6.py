from pylab import *
plt.figure()
x = linspace(2,8,4)
y = x**2
plt.plot(x,y,"r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico")
plt.figure(1)
plt.title("Titulo")
plt.show()