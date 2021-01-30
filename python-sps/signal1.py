import matplotlib.pyplot as plot
import math
xs=[]
ys=[]
for x in range(1000):
    xs.append(0.01*x)
    ys.append(math.sin(xs[x]))
plot.xlabel("time")
plot.ylabel("amplitude")
plot.plot(xs,ys)
plot.show()