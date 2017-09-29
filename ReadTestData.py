import re

file = open("./matchDataTest.csv")
fileToWirte = open("./matchDataTestGet.csv", "w")
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
            fileToWirte.write(match + ",")
    i = 0
    for match in pattern.split(list[3]):
        if match:
            i += 1
            if i == 1:
                fileToWirte.write(match + ",")
            else:
                fileToWirte.write(match)
    fileToWirte.write("\r\n")
file.close()
fileToWirte.close()