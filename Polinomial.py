import numpy as np
import matplotlib.pyplot as plt
import GetData
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score
from sklearn import preprocessing

X = GetData.getData()
y = GetData.getTarget()

x_train, x_test, y_train, y_test = train_test_split(X, y ,test_size=0.1)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=1)
x_poly = poly_reg.fit_transform(x_train)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y_train)
TEST_SIZE = 100
average = 0
for i in range(0, TEST_SIZE):
    x_poly_test = poly_reg.fit_transform(x_test)

    y_predict = lin_reg_2.predict(x_poly_test)

    auc = roc_auc_score(y_test, y_predict)
    average += auc
print average / TEST_SIZE

