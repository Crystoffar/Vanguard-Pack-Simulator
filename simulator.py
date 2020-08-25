import random

def rollNormal():
    randNum = random.randrange(10001)

    if randNum < 168:
        return "RRR"

    if randNum < 668:
        return "RR"

    if randNum < 1167:
        return "R"

    return "C"

def rollFixed():
    randNum = random.randrange(10001)

    if randNum < 168:
        return "RRR"

    if randNum < 668:
        return "RR"

    return "R"

def openPack():
    for i in range(5):
        print(rollNormal())
    print(rollFixed())
    pass

openPack()
