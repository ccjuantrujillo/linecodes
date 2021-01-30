from Tkinter import *
import math

ventana = Tk()
W=800
H=600
cv=Canvas(ventana,width=W,height=H,bg="white")
cv.pack()

cv.create_line(0,H/2,W,H/2)
cv.create_line(W/2,0,W/2,H)
ho=0 
vo=0
vo1=0

x = -2*math.pi

while x <=2*math.pi:
    y = math.sin(x)
    y1 = math.cos(x) 
    h = (W*(x+2*math.pi)/(4*math.pi))
    v = H-(H*(y+1)/2)
    v1 = H-(H*(y1+1)/2)
    cv.create_line(ho,vo,h,v,fill="red") 
    cv.create_line(ho,vo1,h,v1,fill="blue")
    ho=h
    vo=v
    vo1=v1
    x=x+0.1
    
ventana.mainloop()