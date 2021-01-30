import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Importamos al proyecto el dataset boston
boston = load_boston()

#Separamos datos para entrenamiento y datos para testing
x_train,x_test,y_train,y_test = train_test_split(boston['data'],boston['target'])

#Creamos un modelo de regresion lineal
rl = LinearRegression()

#Entrenamos a nuestro algoritmo
rl.fit(x_train,y_train)

#Probamos el modelo con los datos de prueba para que estime el resultado
predicciones = rl.predict(x_test)

#Medimos el aprendizae de nuestro algoritnmo
aprendizaje = rl.score(x_test,y_test)

#Visualizamos las caracteristicas que influeye en el precio del departamento
#El precio de denta del departmento [P.VENTA]
#Los valores predichos por el algoritmo [PREDICCIONES]
df = pd.DataFrame(x_test,columns=boston.feature_names)
df['P.VENTA'] = y_test
df['PREDICCIONES'] = predicciones
print(df)

#Calculamos el desvio
desvio = np.mean(y_test-predicciones)
print("Desviacion: ",desvio)

#Observamos la eficiencia del aprendizaje
print("Efectividad de aprendizaje: ",aprendizaje*100,"%")