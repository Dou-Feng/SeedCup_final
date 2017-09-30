#coding=utf-8
import numpy as np
import GetData
from sklearn import preprocessing
import matplotlib
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import roc_auc_score
from keras.models import Sequential
from keras.layers import Dense, Activation
import GetTeamData

data_X = GetData.getData()
# data_X = preprocessing.scale(data_X)
data_y = GetData.getTarget()

TrainTime = 300
model = LinearRegression()
model.fit(data_X, data_y)

#AUC
TestTime = 10000

average = 0
for i in range(0, TestTime) :
    x_train, x_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.128)
    y_predit = model.predict(x_test)
    auc = roc_auc_score(y_test, y_predit)
    average += auc
print average / TestTime


file = open("./matchDataTestGet.csv")
fileToWrite = open("./predictPro.csv", "w")
line = file.readline()
dataList = []
teamDataList = GetTeamData.TeamData()
scoreList = []
allDataList = []
while line:
    list = line.split(",")
    team = GetData.getTeam(int(list[0]), teamDataList)
    scoreList.append(team.all_importance)
    scoreList.append(team.shootAb)
    scoreList.append(team.threeShootAb)
    scoreList.append(team.bbAb)
    scoreList.append(team.penaltyAb)
    scoreList.append(team.attackAb)
    scoreList.append(team.defendAb)
    scoreList.append(team.sideEffectAb)
    scoreList.append(team.scoreAb)

    scoreList.append(team.hitRate)
    scoreList.append(team.hitTime)
    scoreList.append(team.shootTime)
    scoreList.append(team.threeHitRate)
    scoreList.append(team.threeHitTime)
    scoreList.append(team.threeShootTime)
    scoreList.append(team.penaltyRate)
    scoreList.append(team.penaltyHitTime)
    scoreList.append(team.penaltyTime)
    scoreList.append(team.backboard)
    scoreList.append(team.forwardBB)
    scoreList.append(team.backBB)
    scoreList.append(team.support)
    scoreList.append(team.steal)
    scoreList.append(team.block)
    scoreList.append(team.lose)
    scoreList.append(team.charge)

    team = GetData.getTeam(int(list[1]), teamDataList)
    scoreList.append(team.all_importance)
    scoreList.append(team.shootAb)
    scoreList.append(team.threeShootAb)
    scoreList.append(team.bbAb)
    scoreList.append(team.penaltyAb)
    scoreList.append(team.attackAb)
    scoreList.append(team.defendAb)
    scoreList.append(team.sideEffectAb)
    scoreList.append(team.scoreAb)

    scoreList.append(team.hitRate)
    scoreList.append(team.hitTime)
    scoreList.append(team.shootTime)
    scoreList.append(team.threeHitRate)
    scoreList.append(team.threeHitTime)
    scoreList.append(team.threeShootTime)
    scoreList.append(team.penaltyRate)
    scoreList.append(team.penaltyHitTime)
    scoreList.append(team.penaltyTime)
    scoreList.append(team.backboard)
    scoreList.append(team.forwardBB)
    scoreList.append(team.backBB)
    scoreList.append(team.support)
    scoreList.append(team.steal)
    scoreList.append(team.block)
    scoreList.append(team.lose)
    scoreList.append(team.charge)

    for i in range(2, 6):
        dataList.append(int(list[i]))
    scoreList.append(dataList[0] * dataList[3] - dataList[1] * dataList[2])
    if (dataList[0] + dataList[1] != 0):
        scoreList.append(dataList[0] / (dataList[1] + dataList[0]))
    else:
        scoreList.append(0.0)
    if (dataList[2] + dataList[3]) != 0:
        scoreList.append(dataList[2] / (dataList[2] + dataList[3]))
    else:
        scoreList.append(0.0)
    dataList = dataList + scoreList
    # print dataList
    allDataList.append(dataList)
    scoreList = []
    dataList = []
    line = file.readline()
data_Test = np.array(allDataList)
# data_Test = preprocessing.scale(data_Test)

data_y_Test = model.predict(data_Test)
fileToWrite.write("主场赢得比赛的置信度\r\n")
for i in data_y_Test:
    fileToWrite.write(str(i) + "\r\n")
file.close()
fileToWrite.close()