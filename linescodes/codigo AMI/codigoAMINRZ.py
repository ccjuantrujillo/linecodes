#Densidad espectral de potencia codigo de linea AMI-NRZ
import matplotlib.pyplot as plt#Libreria para generar graficos en 2D
import scipy.fftpack as fourier#librerìa scipy incluye algoritmos para calcular la transformada rapida de fourier
import numpy as np#Librerìa que agrega soporte para vectores y matrices

#Ingresamos parametros para la señal
Vb=input("Ingrese la velocidad binaria(bps): " );
A=input("Ingrese la amplitud de la señal(v): ");
tb=1.0/int(Vb);#Tiempo de bit
tau=tb;#Ancho de pulso tau
BWs=1/tau;#Ancho de banda
paso=tb/100;#Tiempo de paso
t=np.arange(0,tb,paso);#Vector de tiempo hasta 1 tiempo de bit
s1=np.ones(len(t),dtype=int);#Dibujamos un vector de unos de tamaño un tiempo de bit
s0=np.zeros(len(t));#Dibujamos un vector de ceros de tamaño 1 tiempo de bit
n=10;
x=np.random.randint(2,size=n);#Generamos una secuencia de bits aleatoria de tamaño n
print("SOL:");
print("Secuencia binaria: " + str(x));
secuencia = [];#vector donde se almacena la secuencia de bits
for i in range(n):#Dibujamos la secuncia de bits
    if x[i]==1:
        secuencia=np.append(secuencia,s1*int(A));#Dibujamos un 1
    else:
        secuencia=np.append(secuencia,s0);#Dibujamos un 0

t1=(len(secuencia))*paso;#Tiempo final donde termina la secuecia de bits
tt=np.arange(0,t1,paso);#Vector de tiempo
plt.figure(figsize=(7,8));#Crear una nueva figura
plt.subplot(2,1,1)#Generamos el espacio para la imagen superior de la primera figura
plt.plot(tt,secuencia,color='blue');#Graficamos la secuencia de bits
plt.axis([0,t1,-0.2*int(A),1.2*int(A)]);#Colocamos los limites de nuestra grafica
plt.grid(linestyle='-')#Colocamos un grid
plt.title('Codigo UNIPOLAR NRZ');#Titulo de la grafica
#plt.xlabel('Tiempo en (s)');#Etiqueta en el eje x
plt.ylabel("Amplitud en voltios");#Etiqueta en el eje y
#print("Código NRZ");
#print("Tb: %E" % tb);
#print("tau: %E" % tau);
#print("BWs: %E" % BWs);

#Codigo de linea AMI NRZ
tbm=tb;#Tiempo de bit para AMI NRZ igual al tiempo de bit de la señal inicial
taum=tb;#Ancho de pulso tau
BWsm=1/tau;#Ancho de banda
tm=np.arange(0,tbm,paso);#Vector de tiempo hasta 1 tiempo de bit
secuenciaM=[];#Vector donde se almacenara la secuencia de bits AMI NRZ
j=0;
for i in range(n):#Dibujamos la secuencia de bits
    if x[i]==1:
        j=j+1;
        if j%2==0:#Si es par pone -1
            s1M=-int(A)*np.ones(len(tm));
        else:#Si es impar pone un 1
            s1M=int(A)*np.ones(len(tm));
        secuenciaM=np.append(secuenciaM,s1M);
    else:
        s0M=np.zeros(len(tm));
        secuenciaM=np.append(secuenciaM,s0M);
t2=(len(secuenciaM))*paso;#Tiempo final donde termina la secuencia de bits
tt2=np.arange(0,t2,paso);#Vector de tiempo señal AMI NRZ
plt.subplot(2,1,2);#Generamos el espacio para almacenar la imagen ingerior
plt.plot(tt2,secuenciaM,color='red');#Graficamos la secuencia de bits
plt.axis([0,t1,-1.2*int(A),1.2*int(A)]);#Colocamos los limites de nuestra grafica
plt.grid(True)
plt.title('Codigo AMI NRZ');#Titulo de la grafica
#plt.xlabel('Tiempo en (s)');#Etiqueta en el eje x
plt.ylabel("Amplitud en voltios")#Etiqueta en el eje y
print("Tb: %E" % tbm);
print("tau: %E" % taum);
print("BWs: %E" % BWsm);

#Densidad espectral de potencia
plt.figure(2);#Creamos una nueva figura
N=len(tt2);#Cantidad de elementos del vector tt2
S=fourier.fftshift(secuenciaM);#Transformada de fourier
S=fourier.fft(S);
S=fourier.fftshift(S);
fo=1/(N*paso);#Frecuencia de paso
F=np.arange(-N/2,N/2,1);#Vector de frecuencias
#plt.subplot(211);
plt.plot(F,np.abs(S));#Graficamos la densidad espectral de potencia
plt.axis([-50,50,0,np.amax(abs(S))]);
#plt.subplot(212);
#plt.psd(secuenciaM,1024, 1/0.01);
#plt.xlabel('Frequencia')
#plt.ylabel('PSD(db)')
#plt.axis([0,10,0,3]);
input("Press Enter to continue...");
plt.show()

