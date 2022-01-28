import fileHandling as fh

currentDir = str(fh.getPathToCurrentDir())
#rcLocalFile = currentDir + "rc.local"
rcLocalFile = "/etc/" + "rc.local"
contentsFromFile = fh.readTXTFile(rcLocalFile)
nameOfProjectFolder = "IPdisplayscreen"
print("Working from: " + currentDir)

def splitDir():
    newList = currentDir.split(fh.detectOS())
    pathString = ""
    print("Getting path")
    try:
        if newList[len(newList) - 3] == nameOfProjectFolder and newList[len(newList) - 2] == "src":
            for i in range(len(newList) - 1):
                line = newList[i]
                if newList[i] == "":
                    continue
                elif newList[i] == "src" and newList[i - 1] == nameOfProjectFolder:
                    line = ""
                if i == len(newList) - 2:
                    pass
                    #line = line + fh.detectOS()
                pathString = pathString + fh.detectOS() + line
    except:
        print("There was an error.")
        print("Now need to manually go to /etc/rc.local file and add start.sh path before exit and add & after absolute path to start.sh.")
        print("Read 'howtouse.txt' in " + nameOfProjectFolder)
    print("Path: " + pathString)
    return pathString

def addToRcLocal():
    if fh.checkIfFileExist(rcLocalFile):
        if fh.fileContainsString(rcLocalFile, "/" + nameOfProjectFolder + "/start.sh &"): #HUSKA IKKJE KOFFOR
            print("Has already added start script to " + rcLocalFile)
        else:
            for i in range(len(contentsFromFile)):
                try:
                    line = contentsFromFile[i]
                    #print(fh.getLineNumberFromFile(rcLocalFile, "fi"), line == "\n", fh.getLineNumberFromFile(rcLocalFile, "exit 0"), i) 
                    if line == "\n" and i > fh.getLineNumberFromFile(rcLocalFile, "fi")[0] and i < fh.getLineNumberFromFile(rcLocalFile, "exit 0")[0]:
                        if not fh.fileContainsString(rcLocalFile, "IPdisplayscreen/src/mainprogram.py &"):
                            print("Adding file to line >> " + rcLocalFile)
                            fh.replaceLineInFile(rcLocalFile, i, "\npython3 " + splitDir() + "src/mainprogram.py &\n")
                            break
                except Exception as e:
                    print(e)
                    print("There was an error.")
                    print("Now need to manually go to /etc/rc.local file and add start.sh path before exit and add & after absolute path to start.sh.")
                    print("Read 'howtouse.txt' in " + nameOfProjectFolder)

addToRcLocal()