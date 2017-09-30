#coding=utf-8
import numpy as np
import GetData
from sklearn import preprocessing
import matplotlib
from sklearn.cross_validation import  train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import roc_auc_score
from keras.models import Sequential
from keras.layers import Dense, Activation

X = GetData.getData()
X = preprocessing.scale(X)

print X[1]
y = GetData.getTarget()

TrainTime = 300
model = LinearRegression()
# model.add(Dense(1, input_dim=22))
model.fit(X, y)
# model.compile(loss= 'mse', optimizer='sgd')
#
#
# print ('Training----------')
# for step in range(0, TrainTime) :
#
#     cost = model.train_on_batch(X, y)
#
#     if step % 10 == 0:
#         print('train cost:', cost)

#test


#AUC
TestTime = 1000
list_x = []
list_y = []
average = 0
for i in range(0, TestTime) :
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.128)
    y_predit = model.predict(x_test)
    auc = roc_auc_score(y_test, y_predit)
    average += auc
    list_x.append(i)
    list_y.append(auc)


print average / TestTime

