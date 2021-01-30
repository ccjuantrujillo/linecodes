import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [1,2,2,4,5,4,6,4,7,9,10,11,12,10,8]
n = len(x)
x = np.array(x)
y = np.array(y)
sumx = sum(x)
sumy = sum(y)
sumx2 = sum(x*x)
sumy2 = sum(y*y)
sumxy = sum(x*y)
promx = sumx/n
promy = sumy/n
m = (sumx*sumy - n*sumxy)/(sumx**2-n*sumx2)
b = promy - m*promx
sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx*promy
R2 = (sigmaxy/(sigmax*sigmay))**2
print(R2)
plt.plot(x,y,'o',label='Datos')
plt.plot(x,m*x+b,label='Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mi primera regresion')
plt.grid()
plt.legend(loc=4)
plt.show()