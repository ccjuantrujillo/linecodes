from pylab import *
impr = ["b/n","color","duplex","A3"]
vol = [25,31,46,10]
expl = [0,0.02,0,0]
pie(vol,explode=expl,labels=impr,autopct='%1.1f%%',shadow=True)
plt.title("Impresion",bbox={"facecolor":"0.8","pad":5})
plt.legend()
plt.show()