import numpy as np
import pylab as pl
from sklearn import datasets,linear_model
import random

#Datos
x1 = [[0.4],[1.1],[2.1],[2.9],[3.1],[4.2],[4.5]]
y1 = [0.6,1.0,1.9,3.2,3.0,4.1,4.4]

#Crear un objeto de regresion lineal
regr = linear_model.LinearRegression()

regr.fit(x1,y1)

print('Coefficientes: \n',regr.coef_,regr.intercept_)
pl.figure(1)
pl.plot(x1,regr.predict(x1),color='black',linewidth=3)
pl.scatter(x1,y1,s=40,marker='o',color='k')
pl.xlabel('X')
pl.ylabel('Y')
pl.xlim(0.0,5.0)
pl.ylim(0.0,5.0)
pl.show()