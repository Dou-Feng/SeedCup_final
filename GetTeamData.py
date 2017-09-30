# player_ability
#coding=utf-8

K_SHOT_TIME = 0.01
K_SHOT_RATE = 0.3
K_THREESHOT_RATE = 0.5
K_THREESHOT_TIME = 0.07
K_F_BB = 0.10
K_B_BB = 0.06
K_SCORE = 0.12
K_LOSE = -0.05
K_BLOCK = 0.11
K_STEAL = 0.16
K_CHARGE = -0.03
K_PENALTY_TIME = 0.01
K_PENALTY_RATE = 0.1
K_SHOW = 0.01
K_FIRST_SHOW = 0.02
K_SHOWTIME_ALL = 0.01
K_SUPPORT = 0.03

# player_in_team
class Player:
    "Use self class to reserve the data in the list"
    teamNumber = 0
    number = 0
    showUpTime = 0
    firstShowUpTime = 0
    playTime = 0
    hitRate = 0
    hitTime = 0
    shootTime = 0
    threeHitRate = 0
    threeHitTime = 0
    threeShootTime = 0
    penaltyRate = 0
    penaltyHitTime = 0
    penaltyTime = 0
    backboard = 0
    forwardBB = 0
    backBB = 0
    support = 0
    steal = 0
    block = 0
    lose = 0
    charge = 0
    # ablity cal
    importance = 0
    shootAb = 0
    threeShootAb = 0
    penaltyAb = 0
    bbAb = 0
    scoreAb = 0
    attackAb = 0
    defendAb = 0
    sideEffectAb = 0

    def cal_ability(self):
        self.importance = K_SHOW * self.showUpTime + K_FIRST_SHOW * self.firstShowUpTime + K_SHOWTIME_ALL * self.playTime
        self.shootAb = K_SHOT_RATE * self.hitRate + K_SHOT_TIME * self.hitTime
        self.threeShootAb = K_SHOT_RATE * self.threeHitRate
        self.bbAb = K_B_BB * self.backBB + K_F_BB * self.forwardBB
        self.penaltyAb = K_PENALTY_RATE * self.penaltyRate + K_PENALTY_TIME * self.penaltyHitTime
        self.scoreAb = K_SCORE * self.score + K_CHARGE * self.charge + K_LOSE * self.lose + K_BLOCK * self.block + K_STEAL * self.steal
        self.attackAb = K_SHOT_TIME * self.shootTime + K_THREESHOT_TIME * self.threeShootTime + K_SCORE * self.score
        self.defendAb = K_BLOCK * self.block + K_STEAL * self.steal
        self.sideEffectAb = K_CHARGE * self.charge + K_LOSE * self.lose
        self.hitRate *= K_SHOT_RATE
        self.hitTime *= K_SHOT_TIME
        self.shootTime *= K_SHOT_TIME
        self.threeHitRate *= K_THREESHOT_RATE
        self.threeHitTime *= K_SHOT_TIME
        self.threeShootTime *= K_THREESHOT_TIME
        self.penaltyRate *= K_PENALTY_RATE
        self.penaltyHitTime *= K_PENALTY_TIME
        self.penaltyTime *= K_PENALTY_TIME
        self.backboard *= K_B_BB
        self.forwardBB *= K_F_BB
        self.backBB *= K_B_BB
        self.support *= K_SUPPORT
        self.steal *= K_STEAL
        self.block *= K_BLOCK
        self.lose *= K_LOSE
        self.charge *= K_CHARGE

    def __init__(self, list):
        self.teamNumber = int(list[0])
        self.number = int(list[1])
        self.showUpTime = int(list[2])
        self.firstShowUpTime = int(list[3])
        self.playTime = float(list[4])
        if list[5] != "":
            tempRate = list[5].strip('%')
        else:
            tempRate = 0
        self.hitRate = float(tempRate) / 100
        self.hitTime = float(list[6])
        self.shootTime = float(list[7])
        if list[8] != "":
            tempRate = list[8].strip('%')
        else:
            tempRate = 0
        self.threeHitRate = float(tempRate) / 100
        self.threeHitTime = float(list[9])
        self.threeShootTime = float(list[10])
        if list[11] != "":
            tempRate = list[11].strip('%')
        else:
            tempRate = 0
        self.penaltyRate = float(tempRate) / 100
        self.penaltyHitTime = float(list[12])
        self.penaltyTime = float(list[13])
        self.backboard = float(list[14])
        self.forwardBB = float(list[15])
        self.backBB = float(list[16])
        self.support = float(list[17])
        self.steal = float(list[18])
        self.block = float(list[19])
        self.lose = float(list[20])
        self.charge = float(list[21])
        self.score = float(list[22])
        self.cal_ability()


class Team:
    number = 0


    def __init__(self, number):
        self.number = number
        self.players = []
        self.all_importance = 0
        self.shootAb = 0
        self.threeShootAb = 0
        self.bbAb = 0
        self.penaltyAb = 0
        self.attackAb = 0
        self.defendAb = 0
        self.sideEffectAb = 0
        self.scoreAb = 0

        self.hitRate = 0
        self.hitTime = 0
        self.shootTime = 0
        self.threeHitRate = 0
        self.threeHitTime = 0
        self.threeShootTime = 0
        self.penaltyRate = 0
        self.penaltyHitTime = 0
        self.penaltyTime = 0
        self.backboard = 0
        self.forwardBB = 0
        self.backBB = 0
        self.support = 0
        self.steal = 0
        self.block = 0
        self.lose = 0
        self.charge = 0

    def add_player(self, player):
        self.players.append(player)
        self.all_importance += player.importance

    def calTeamAb(self):
        for player in self.players:
            self.shootAb += player.importance * player.shootAb / self.all_importance
            self.threeShootAb += player.importance * player.threeShootAb / self.all_importance
            self.bbAb += player.importance * player.bbAb / self.all_importance
            self.penaltyAb += player.importance * player.penaltyAb / self.all_importance
            self.attackAb += player.importance * player.attackAb / self.all_importance
            self.defendAb += player.importance * player.defendAb /self.all_importance
            self.sideEffectAb += player.importance * player.sideEffectAb / self.all_importance
            self.scoreAb += player.importance * player.scoreAb / self.all_importance

            self.hitRate += player.importance * player.hitRate / self.all_importance
            self.hitTime += player.importance * player.hitTime / self.all_importance
            self.shootTime += player.importance * player.shootTime / self.all_importance
            self.threeHitRate += player.importance * player.threeHitRate / self.all_importance
            self.threeHitTime += player.importance * player.threeHitTime / self.all_importance
            self.threeShootTime += player.importance * player.threeShootTime / self.all_importance
            self.penaltyRate += player.importance * player.penaltyRate / self.all_importance
            self.penaltyHitTime += player.importance * player.penaltyHitTime / self.all_importance
            self.penaltyTime += player.importance * player.penaltyTime / self.all_importance
            self.backboard += player.importance * player.backboard / self.all_importance
            self.forwardBB += player.importance * player.forwardBB / self.all_importance
            self.backBB += player.importance * player.backBB / self.all_importance
            self.support += player.importance * player.support / self.all_importance
            self.steal += player.importance * player.steal / self.all_importance
            self.block += player.importance * player.block / self.all_importance
            self.lose += player.importance * player.lose / self.all_importance
            self.charge += player.importance * player.charge / self.all_importance


def TeamData():
    teamData = open("./teamData.csv", "r")
    teamData.readline()
    str = teamData.readline()
    str = str.split("\r\n")[0]
    list = str.split(",")
    list_player = []
    list_team = []
    for k in range(0, 208):
        team_temp = Team(k)
        list_team.append(team_temp)
    while str != "":
        player = Player(list)
        temp = 0.0
        #debug player's ab
        # if player.teamNumber == 1:
        #     temp += player.shootAb * player.importance
        # print temp, player.importance, player.shootAb
        list_player.append(player)
        str = teamData.readline()
        str = str.split("\r\n")[0]
        list = str.split(",")
    for player in list_player:
        team_num = player.teamNumber
        team_temp = list_team[team_num]
        team_temp.players.append(player)
        team_temp.all_importance += player.importance
    j = 0
    for team in list_team:
        team.calTeamAb()
        j = j + 1
    return list_team



