import random


def getRandNotEqualTo(start: int, stop: int, notEqual: int):
    x = random.randint(start, stop)
    while x == notEqual:
        x = random.randint(start, stop)
    return x


def randGo(string: str, totalClumps: int, goIndex: int, i: int):
    clumpsize = 12
    if string != "go":
        return f"{string} {clumpsize * i + goIndex}"
    return f"{string} {range(0, totalClumps * clumpsize, clumpsize)[random.randint(0, totalClumps - 1)] + goIndex}"


def initClumps(totalClumps: int, i: int):
    right_or_left = ["right", "left"]
    actions = ["right", "left", "hop"]
    # clump_check = lambda :
    return [randGo("ifenemy", totalClumps, 5, i),
            randGo("ifsame", totalClumps, 7, i),
            randGo("ifwall", totalClumps, 9, i),
            randGo("ifempty", totalClumps, 11, i),
            randGo("infect", totalClumps, 1, i),
            randGo("go", totalClumps, 1, i),
            right_or_left[random.randint(0, 1)],
            randGo("go", totalClumps, 1, i),
            right_or_left[random.randint(0, 1)],
            randGo("go", totalClumps, 1, i),
            actions[random.randint(0, 2)],
            randGo("go", totalClumps, 1, i)]


def writeRandom():
    f = open("texts/oliver.txt", "w")
    genes = 50
    chunks = []
    list1 = []
    for i in range(genes):
        chunk = initClumps(genes, i)
        chunks.append(chunk)
    for i in chunks:
        for j in i:
            f.write(j + "\n")
            list1.append(j)
    f.write("go 1")
    list1.append(j)
    f.close()
    return list1


def mutate(list1: list):
    option = random.randint(0, 1)
    whichGene = random.randint(0, 49)
    if option:
        whichAction = [7, 9, 11][random.randint(0, 2)]
        index = whichGene * 12 + whichAction - 1
        if whichAction != 11:
            list1[index] = "right" if list1[index] == "left" else "left"
            return list1
        else:
            list1[index] = ["right", "left"][random.randint(0, 1)] if list1[index] == "hop" else ["right", "hop"][random.randint(0, 1)] if list1[index] == "left" else ["left", "hop"][random.randint(0, 1)]
            return list1
    else:
        whichAction = [6, 8, 10, 12][random.randint(0, 3)]
        index = whichGene * 12 + whichAction - 1
        newGoIndex = random.randint(0, 49) * 12 + 1
        while newGoIndex == int(list1[index].split()[1]):
            newGoIndex = random.randint(0, 49) * 12 + 1
        list1[index] = f"go {newGoIndex}"
        return list1
