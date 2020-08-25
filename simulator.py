import random
import csv

fileName = "01_king_of_knights.csv"

CList = []
RList = []
RRList = []
RRRList = []

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

def rollNormal():
    randNum = random.randrange(10001)

    if randNum < 168:
        cardNum = random.randrange(len(RRRList))
        print("[RRR] " + RRRList[cardNum])
        return

    if randNum < 668:
        cardNum = random.randrange(len(RRList))
        print("[RR] " + RRList[cardNum])
        return

    if randNum < 1167:
        cardNum = random.randrange(len(RList))
        print("[R] " + RList[cardNum])
        return

    cardNum = random.randrange(len(CList))
    print("[C] " + CList[cardNum])

def rollFixed():
    randNum = random.randrange(10001)

    if randNum < 168:
        cardNum = random.randrange(len(RRRList))
        print("[RRR] " + RRRList[cardNum])
        return

    if randNum < 668:
        cardNum = random.randrange(len(RRList))
        print("[RR] " + RRList[cardNum])
        return

    cardNum = random.randrange(len(RList))
    print("[R] " + RList[cardNum])

def openPack():
    for i in range(5):
        rollNormal()
    rollFixed()

importSet()
openPack()
