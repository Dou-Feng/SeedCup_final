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

    fileMatch = open("./matchDataGet.csv")
    teamList = GetTeamData.TeamData()
    line = fileMatch.readline()
    while line:
        dataList = []
        scoreList = []
        lineList = line.split(",")
        for i in range(0, 6):
            dataList.append(int(lineList[i]))
        # if dataList[3] !=0:
        #     scoreList.append(dataList[2]/dataList[3])
        # elif dataList[3] =
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

        
        del dataList[0]
        del dataList[0]
        dataList = dataList + scoreList
        allDataList.append(dataList)
        line = fileMatch.readline()
    data = np.array(allDataList)
    return data
