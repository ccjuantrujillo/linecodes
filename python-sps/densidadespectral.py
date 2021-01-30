#Densidad espectral de potencia
plt.figure(2);
n=1024;
dp=0.5/1024;
t=np.arange(-0.5,0.5,dp);
xanalog=np.zeros(len(t),dtype=float);
for i in range(0,len(t)):
    xanalog[i] = np.sin(2 * np.pi * i/500)
xf=fourier.fft(xanalog[n:2*n]);
xf=fourier.fftshift(xf);
xfabs=(1/n)*np.abs(xf);
frq=fourier.fftfreq(n,0.5/n);
frq=fourier.fftshift(frq);
plt.subplot(2,1,1);
plt.plot(t,xanalog);
plt.subplot(2,1,2);
plt.plot(frq,xfabs);
plt.show()