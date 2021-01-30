import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

boston = datasets.load_boston()
boston_df = pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df['TARGET']=boston.target
boston_df.head()

r1 = LinearRegression()
r1.fit(boston.data,boston.target)

LinearRegression(copy_X=True,fit_intercept=True,n_jobs=1,normalize=False)
atrib = list(zip(boston.feature_names,r1.coef_))
print(atrib)