#Densidad espectral de potencia codigo de linea AMI-NRZ
import matplotlib.pyplot as plt#Libreria para generar graficos en 2D
import scipy.fftpack as fourier#librerìa scipy incluye algoritmos para calcular la transformada rapida de fourier
import numpy as np#Librerìa que agrega soporte para vectores y matrices

#Ingresamos parametros para la señal
Vb=input("Ingrese la velocidad binaria(bps): " );
A=input("Ingrese la amplitud de la señal(v): ");
tb=1.0/int(Vb);#Tiempo de bit
paso=tb/100;#Tiempo de paso
t=np.arange(0,tb,paso);#Vector de tiempo hasta 1 tiempo de bit
s1=np.ones(len(t),dtype=int);#Dibujamos un vector de unos de tamaño un tiempo de bit
s0=np.zeros(len(t));#Dibujamos un vector de ceros de tamaño 1 tiempo de bit
#Secuencia aleatoria de bits
n=10;
x=np.random.randint(2,size=n);#Generamos una secuencia de bits aleatoria de tamaño n
secuencia = [];#vector donde se almacena la secuencia de bits
for i in range(n):#Dibujamos la secuncia de bits
    if x[i]==1:
        secuencia=np.append(secuencia,s1);#Dibujamos un 1
    else:
        secuencia=np.append(secuencia,s0);#Dibujamos un 0

t1=(len(secuencia))*paso;#Tiempo final donde termina la secuecia de bits
tt=np.arange(0,t1,paso);#Vector de tiempo
plt.figure(1);#Crear una nueva figura
plt.subplot(2,1,1)#Generamos el espacio para la imagen superior de la primera figura
plt.plot(tt,secuencia,color='blue');#Graficamos la secuencia de bits
plt.axis([0,t1,-0.5,1.5]);#Colocamos los limites de nuestra grafica
plt.grid(linestyle='-')#Colocamos un grid
plt.title('Codigo UNIPOLAR NRZ');#Titulo de la grafica
#plt.xlabel('Tiempo en (s)');#Etiqueta en el eje x
plt.ylabel("Amplitud en voltios");#Etiqueta en el eje y

#Codigo de linea AMI NRZ
tbm=tb;#Tiempo de bit para AMI NRZ igual al tiempo de bit de la señal inicial
tm=np.arange(0,tbm,paso);#Vector de tiempo hasta 1 tiempo de bit
secuenciaM=[];#Vector donde se almacenara la secuencia de bits AMI NRZ
j=0;
for i in range(n):#Dibujamos la secuencia de bits
    if x[i]==1:
        j=j+1;
        if j%2==0:#Si es par pone -1
            s1M=-np.ones(len(tm));
        else:#Si es impar pone un 1
            s1M=np.ones(len(tm));
        secuenciaM=np.append(secuenciaM,s1M);
    else:
        s0M=np.zeros(len(tm));
        secuenciaM=np.append(secuenciaM,s0M);
t2=(len(secuenciaM))*paso;#Tiempo final donde termina la secuencia de bits
tt2=np.arange(0,t2,paso);#Vector de tiempo señal AMI NRZ
plt.subplot(2,1,2);#Generamos el espacio para almacenar la imagen ingerior
plt.plot(tt2,secuenciaM,color='red');#Graficamos la secuencia de bits
plt.axis([0,t1,-1.5,1.5]);#Colocamos los limites de nuestra grafica
plt.grid(True)
plt.title('Codigo AMI NRZ');#Titulo de la grafica
#plt.xlabel('Tiempo en (s)');#Etiqueta en el eje x
plt.ylabel("Amplitud en voltios")#Etiqueta en el eje y

#Densidad espectral de potencia
plt.figure(2);#Creamos una nueva figura
N=len(tt2);#Cantidad de elementos del vector tt2
S=fourier.fftshift(secuenciaM);#Transformada de fourier
S=fourier.fft(S);
S=fourier.fftshift(S);
fo=1/(N*paso);#Frecuencia de paso
F=np.arange(-N/2,N/2,1);#Vector de frecuencias
plt.plot(F,np.abs(S));#Graficamos la densidad espectral de potencia
plt.show()

