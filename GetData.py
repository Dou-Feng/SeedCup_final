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
        guest_win = dataList[2]
        guset_lose = dataList[3]
        host_win = dataList[4]
        host_lose = dataList[5]
        if (guset_lose != 0) :
            dataList.append(float(guest_win / guset_lose))
        else :
            dataList.append(0.0)

        if (host_lose != 0):
            dataList.append(host_win / host_lose)
        else :
            dataList.append(0.0)
        team = getTeam(int(dataList[0]), teamList)
        scoreList.append(team.all_importance)
        scoreList.append(team.shootAb)
        scoreList.append(team.threeShootAb)
        scoreList.append(team.bbAb)
        scoreList.append(team.penaltyAb)
        scoreList.append(team.attackAb)
        scoreList.append(team.defendAb)
        scoreList.append(team.sideEffectAb)
        scoreList.append(team.scoreAb)
        team = getTeam(int(dataList[1]), teamList)
        scoreList.append(team.all_importance)
        scoreList.append(team.shootAb)
        scoreList.append(team.threeShootAb)
        scoreList.append(team.bbAb)
        scoreList.append(team.penaltyAb)
        scoreList.append(team.attackAb)
        scoreList.append(team.defendAb)
        scoreList.append(team.sideEffectAb)
        scoreList.append(team.scoreAb)
        del dataList[0]
        del dataList[0]
        dataList = scoreList + dataList
        scoreList = []
        allDataList.append(dataList)
        dataList = []
        line = fileMatch.readline()
    data = np.array(allDataList)
    return data