file = open("./teamData.csv")
fileToWrite=open("./teamDataGet.csv","w")
line = file.readline()
percent=0.0
while line:
    line=file.readline()
    if not line:
        break
    list=line.split(",")
    for i in range(0,5):
        fileToWrite.write(list[i]+",")
    if list[5]:
        percent=float(list[5].split("%")[0])
        fileToWrite.write(str(percent/100)+",")
    for i in range(6,8):
        fileToWrite.write(list[i]+",")
    if list[8]:
        percent=float(list[8].split("%")[0])
        fileToWrite.write(str(percent/100)+",")
    for i in range(9,11):
        fileToWrite.write(list[i]+",")
    if list[11]:
        percent=float(list[5].split("%")[0])
        fileToWrite.write(str(percent/100)+",")
    for i in range(12,22):
        fileToWrite.write(list[i]+",")
    fileToWrite.write(list[22]+"\r\n")
file.close()
fileToWrite.close()