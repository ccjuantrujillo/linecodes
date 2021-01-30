import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge

#Cargamos y preparamos el dataSet
boston = load_boston()
boston.keys()
boston.target.shape

#Separamos datos para entrenamiento y datos para testing
x_ent,x_test,y_ent,y_test = train_test_split(boston.data,boston.target)
x_ent.shape
y_ent.shape

knn = KNeighborsRegressor(n_neighbors=5)

knn.fit(x_ent,y_ent)

res = knn.score(x_test,y_test)

del knn

rl= LinearRegression()
rl.fit(x_ent,y_ent)
res = rl.score(x_test,y_test)

del rl
ridge = Ridge(alpha=.5)
ridge.fit(x_ent,y_ent)
res = ridge.score(x_test,y_test)

print(res)
