import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#Importamos al proyecto el dataset iris
iris = load_iris()

#Separamos datos para entrenamiento y datos para testing
x_train,x_test,y_train,y_test = train_test_split(iris['data'],iris['target'])

#Creamos nuestro modelo
knn = KNeighborsClassifier(n_neighbors=7) #7numeros mas cercanos

#Entrenamos a nuestro algoritmo
knn.fit(x_train,y_train)

#Probamos el modelo con los datos de prueba para que estime el resultado
predicciones = knn.predict(x_test)

#Medimos el aprendizae de nuestro algoritnmo
aprendizaje = knn.score(x_test,y_test)

#Visualizamos las caracteristicas que influeye en el precio del departamento
#El precio de denta del departmento [P.VENTA]
#Los valores predichos por el algoritmo [PREDICCIONES]
df = pd.DataFrame(x_test,columns=iris.feature_names)
df['TIPO DE FLOR'] = y_test
df['PREDICCIONES'] = predicciones
print(df)

#Calculamos el desvio
desvio = np.mean(y_test-predicciones)
print("Desviacion: ",desvio)

#Observamos la eficiencia del aprendizaje
print("Efectividad de aprendizaje: ",aprendizaje*100,"%")