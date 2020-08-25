import random
import csv

fileName = "01_king_of_knights.csv"

CList = []
RList = []
RRList = []
RRRList = []

exportDict = dict()

def importSet():
    setCSV = open(fileName, "r")
    dataReader = csv.reader(setCSV)
    data = []
    for row in dataReader:
        data.append(row)

    for row in range(len(data)):
        if data[row][0] == "C":
            CList.append(data[row][1])
        if data[row][0] == "R":
            RList.append(data[row][1])
        if data[row][0] == "RR":
            RRList.append(data[row][1])
        if data[row][0] == "RRR":
            RRRList.append(data[row][1])

def addCard(cardName):
    if cardName in exportDict:
        exportDict[cardName] += 1
    else:
        exportDict[cardName] = 1

def rollNormal():
    randNum = random.randrange(10001)

    if randNum < 168:
        cardNum = random.randrange(len(RRRList))
        print("[RRR] " + RRRList[cardNum])
        addCard(RRRList[cardNum])
        return

    if randNum < 668:
        cardNum = random.randrange(len(RRList))
        print("[RR] " + RRList[cardNum])
        addCard(RRList[cardNum])
        return

    if randNum < 1167:
        cardNum = random.randrange(len(RList))
        print("[R] " + RList[cardNum])
        addCard(RList[cardNum])
        return

    cardNum = random.randrange(len(CList))
    print("[C] " + CList[cardNum])
    addCard(CList[cardNum])

def rollFixed():
    randNum = random.randrange(10001)

    if randNum < 168:
        cardNum = random.randrange(len(RRRList))
        print("[RRR] " + RRRList[cardNum])
        addCard(RRRList[cardNum])
        return

    if randNum < 668:
        cardNum = random.randrange(len(RRList))
        print("[RR] " + RRList[cardNum])
        addCard(RRList[cardNum])
        return

    cardNum = random.randrange(len(RList))
    print("[R] " + RList[cardNum])
    addCard(RList[cardNum])

def openPack():
    for i in range(5):
        rollNormal()
    rollFixed()

def openBox():
    for i in range(30):
        answer = "n"
        while answer != "y" and "Y":
            openPack()
            print("You have opened %s / 30 packs" %(i + 1))
            if i != 29:
                answer = input("Open next pack? (Y/N) ")
            else:
                answer = input("Finish? (Y/N) ")

def exportPulls():
    exportCSV = "pulls.csv"
    try:
        with open(exportCSV, 'w') as csvFile:
            writer = csv.writer(csvFile)
            for cardName, quantity in exportDict.items():
                writer.writerow([cardName, quantity])
    except IOError:
        print("I/O error")

#Main
importSet()
openBox()
exportPulls()
