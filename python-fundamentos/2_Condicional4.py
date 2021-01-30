#control
import signal
import numpy as np

def series(sys1,sys2):
    if not isinstance(sys1,signal.lti):
        sys1 = signal.lti(*sys1)
    if not isinstance(sys2,signal.lti):
        sys2 = signal.lti(*sys2)
    num = np.polymul(sys1.num,sys2.num)
    den = np.polymul(sys1.den,sys2.den)
    sys = signal.lti(num,den)
    return  sys

#Programa aca empieza
k=200
series([k],[1]),sys_car)