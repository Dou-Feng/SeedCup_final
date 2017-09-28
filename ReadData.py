import re

file = open("/home/cainot/Documents/matchDataTrain.csv")
fileToWirte = open("/home/cainot/Documents/matchDataGet.csv", "w")
line = file.readline()
pattern = re.compile("\D")
while line:
    line = file.readline()
    if not line:
        break
    list = line.split(",")
    fileToWirte.write(list[0] + "," + list[1] + ",")
    for match in pattern.split(list[2]):
        if match:
            fileToWirte.write(match + ","),
    for match in pattern.split(list[3]):
        if match:
            fileToWirte.write(match + ",")
    i = 0
    score = 0
    scoreHost = 0
    scoreCustom = 0
    for match in list[4].split(":"):
        if match:
            i += 1
            if i == 1:
                scoreCustom = int(match)
            else:
                scoreHost = int(match)
    fileToWirte.write(str(scoreCustom - scoreHost))
    fileToWirte.write("\r\n")
file.close()
fileToWirte.close()