import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('boston.csv',sep=";")
print(df['MV'])
plt.hist(df['MV'])

plt.show()