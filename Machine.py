#coding=utf-8
import GetTeamData
import numpy as np
import GetData
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
import scipy as sp
from matplotlib import pylab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve, roc_curve, auc
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import time
start_time = time.time()

def plot_pr(auc_score, precision, recall, label=None):
    pylab.figure(num=None, figsize=(6,5))
    pylab.xlim([0.0, 1.0])
    pylab.ylim([0.0, 1.0])
    pylab.xlabel('Recall')
    pylab.ylabel('Precision')
    pylab.title('P/R (AUC=%0.2f) / %s' % (auc_score, label))
    pylab.fill_between(recall, precision, alpha = 0.5)
    pylab.grid(True, linestyle='-', color='0.75')
    pylab.plot(recall, precision, lw=  1)
    pylab.show()

data_X = GetData.getData()
data_X = preprocessing.scale(data_X)
data_y = GetData.getTarget()
#进行交叉验证
count_vec = TfidfVectorizer(binary= False, decode_error='ignore', stop_words='english')
average = 0
testNum = 10
for i in range(0, testNum):
    x_train, x_test, y_train, y_test = train_test_split(data_X, data_y, test_size= 0.1)
    # x_train = count_vec.fit_transform(x_train)
    # x_test = count_vec.transform(x_test)

    #训练LR分类器
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    p = np.mean(y_pred==y_test)

    print (p)
    average += p

answer = clf.predict_proba(x_test)[:,1]
precision, recall, thresholds = precision_recall_curve(y_test, answer)
report = answer > 0.5
print (classification_report(y_test, report, target_names=['neg', 'pos']))
print ("average precision:", average/testNum)
print ("time spent", time.time() - start_time)



plot_pr(0.5, precision, recall, "pos")

file = open("./matchDataTestGet.csv")
fileToWrite = open("./output.csv", "w")










# model = LinearRegression()
# model.fit(data_X, data_y)
# line = file.readline()
# dataList = []
# teamDataList = GetTeamData.TeamData()
# scoreList = []
# allDataList = []
# while line:
#     list = line.split(",")
#     team = GetData.getTeam(int(list[0]), teamDataList)
#     scoreList.append(team.all_importance)
#     scoreList.append(team.shootAb)
#     scoreList.append(team.threeShootAb)
#     scoreList.append(team.bbAb)
#     scoreList.append(team.penaltyAb)
#     scoreList.append(team.attackAb)
#     scoreList.append(team.defendAb)
#     scoreList.append(team.sideEffectAb)
#     team = GetData.getTeam(int(list[1]), teamDataList)
#     scoreList.append(team.all_importance)
#     scoreList.append(team.shootAb)
#     scoreList.append(team.threeShootAb)
#     scoreList.append(team.bbAb)
#     scoreList.append(team.penaltyAb)
#     scoreList.append(team.attackAb)
#     scoreList.append(team.defendAb)
#     scoreList.append(team.sideEffectAb)
#     for i in range(2, 6):
#         dataList.append(int(list[i]))
#     dataList = dataList + scoreList
#     # print dataList
#     allDataList.append(dataList)
#     scoreList = []
#     dataList = []
#     line = file.readline()
# data_Test = np.array(allDataList)
# data_Test = preprocessing.scale(data_Test)
# data_y_Test = model.predict(data_Test)
# for i in data_y_Test:
#     fileToWrite.write(str(i) + "\r\n")
# file.close()
# fileToWrite.close()
