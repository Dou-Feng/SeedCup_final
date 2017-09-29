import numpy as np
import GetTeamData

#Training Y
def getTarget():
    fileMatch = open("./matchDataGet.csv")
    # fileTeam=open("")
    line = fileMatch.readline()
    targetList = []
    while line:
        lineList = line.split(",")
        score = int(lineList[6])
        if score < 0:
            targetList.append(1)
        else:
            targetList.append(0)
        line = fileMatch.readline()
    target = np.array(targetList)
    return target


def getTeam(teamNum, teamList):
    for team in teamList:
        if teamNum == team.number:
            return team

#Training X
def getData():
    allDataList = []
    dataList = []
    scoreList = []
    fileMatch = open("./matchDataGet.csv")
    teamList = GetTeamData.TeamData()
    line = fileMatch.readline()
    while line:
        lineList = line.split(",")
        for i in range(0, 6):
            dataList.append(int(lineList[i]))
        team = getTeam(int(dataList[0]), teamList)
        scoreList.append(team.all_importance)
        scoreList.append(team.shootAb)
        scoreList.append(team.threeShootAb)
        scoreList.append(team.bbAb)
        scoreList.append(team.penaltyAb)
        scoreList.append(team.attackAb)
        scoreList.append(team.defendAb)
        scoreList.append(team.sideEffectAb)
        team = getTeam(int(dataList[1]), teamList)
        scoreList.append(team.all_importance)
        scoreList.append(team.shootAb)
        scoreList.append(team.threeShootAb)
        scoreList.append(team.bbAb)
        scoreList.append(team.penaltyAb)
        scoreList.append(team.attackAb)
        scoreList.append(team.defendAb)
        scoreList.append(team.sideEffectAb)
        del dataList[0]
        del dataList[0]
        dataList = dataList + scoreList
        scoreList = []
        allDataList.append(dataList)
        dataList = []
        line = fileMatch.readline()
    data = np.array(allDataList)
    return data