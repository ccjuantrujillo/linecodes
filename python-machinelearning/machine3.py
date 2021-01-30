from matplotlib import pyplot as plt
from sklearn.datasets import    load_iris

iris = load_iris()
data = iris.data
plt.plot(data[:,0],data[:,1],".")
plt.show()