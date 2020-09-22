#Densidad espectral de potencia codigo de linea AMI-RZ
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

#Ingresamos parametros para la señal
tb=1;
paso=1/100;
t=np.arange(0,tb,paso);
s1=np.ones(len(t),dtype=int);
s0=np.zeros(len(t));
#Secuencia aleatoria de bits
n=10;
x=np.random.randint(2,size=n);
secuencia = [];
for i in range(n):
    if x[i]==1:
        secuencia=np.append(secuencia,s1);
    else:
        secuencia=np.append(secuencia,s0);

t1=(len(secuencia))*paso;
tt=np.arange(0,t1,paso);
plt.figure(1);
plt.subplot(2,1,1)
plt.plot(tt,secuencia,color='blue')
plt.axis([0,t1,-0.5,1.5]);
plt.grid(linestyle='-')
plt.title('Codigo UNIPOLAR NRZ');
#plt.xlabel('Tiempo en (s)');
plt.ylabel("Amplitud en voltios")

#Codigo de linea AMI RZ
tbm=tb/2;
tm=np.arange(0,tbm,paso);
secuenciaM=[];
j=0;
for i in range(n):
    if x[i]==1:
        j=j+1;
        if j%2==0:
            s1M=-np.ones(len(tm));
            s1M=np.append(s1M,np.zeros(len(tm)));
        else:
            s1M=np.ones(len(tm));
            s1M=np.append(s1M, np.zeros(len(tm)));
        secuenciaM=np.append(secuenciaM,s1M);
    else:
        s0M=np.zeros(len(tm));
        s0M=np.append(s0M,np.zeros(len(tm)));
        secuenciaM=np.append(secuenciaM,s0M);
t2=(len(secuenciaM))*paso;
tt2=np.arange(0,t2,paso);
plt.subplot(2,1,2);
plt.plot(tt2,secuenciaM,color='red')
plt.axis([0,t1,-1.5,1.5]);
plt.grid(True)
plt.title('Codigo AMI RZ');
#plt.xlabel('Tiempo en (s)');
plt.ylabel("Amplitud en voltios")

#Densidad espectral de potencia
plt.figure(2);
N=len(tt2);
S=fourier.fftshift(secuenciaM);
S=fourier.fft(S);
S=fourier.fftshift(S);
fo=1/(N*paso);
F=np.arange(-N/2,N/2,1);
plt.plot(F,np.abs(S));
plt.show()

