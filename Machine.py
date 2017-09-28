import numpy as np
import GetData
from sklearn.linear_model import LinearRegression
data_X=GetData.getData()
data_y=GetData.getTarget()
model=LinearRegression()
model.fit(data_X,data_y)
print model.predict(data_X[0:200])