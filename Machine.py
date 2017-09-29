import GetTeamData
import numpy as np
import GetData
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import  train_test_split
from sklearn.neighbors import KNeighborsClassifier

data_X = GetData.getData()
data_X = preprocessing.scale(data_X)
data_y = GetData.getTarget()
# model = LinearRegression()
# model.fit(data_X, data_y)
# file = open("./matchDataTestGet.csv")
# fileToWrite = open("./output.csv", "w")
#
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
#     scoreList.append(team.scoreAb)
#     team = GetData.getTeam(int(list[1]), teamDataList)
#     scoreList.append(team.all_importance)
#     scoreList.append(team.shootAb)
#     scoreList.append(team.threeShootAb)
#     scoreList.append(team.bbAb)
#     scoreList.append(team.penaltyAb)
#     scoreList.append(team.scoreAb)
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
from sklearn.cross_validation import cross_val_score
k_range = range(20, 50)
k_score = []

for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    loss = -cross_val_score(knn, data_X, data_y, scoring='mean_squared_error')
    # scores = cross_val_score(knn, data_X, data_y, cv=10, scoring='accuracy')
    k_score.append(loss.mean())

plt.plot(k_range, k_score)
plt.xlabel('Value of K')
plt.ylabel('Cross-Validated')
plt.show()