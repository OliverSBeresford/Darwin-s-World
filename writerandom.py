import random

# Used to initialize Oliver procedure
# (starts with completely random procedure, that still works, but not well)
# Mutates multiple times, test each mutation, keeps best one, repeats
# Learns --> emergent behavior


#This gets a random number from start to stop not equal to notEqual
def getRandNotEqualTo(start: int, stop: int, notEqual: int):
    x = random.randint(start, stop)
    while x == notEqual:
        x = random.randint(start, stop)
    return x


# returns an f string in the format of:
# [action] if action doesn't go to a new line in procedure
# [[action] [go to goIndex withn any clump within the procedure]]
# See below for what a clump is
def randAction(string: str, totalClumps: int, goIndex: int, i: int):
    clumpsize = 12
    if string != "go":
        return f"{string} {clumpsize * i + goIndex}"
    return f"{string} {range(0, totalClumps * clumpsize, clumpsize)[random.randint(0, totalClumps - 1)] + goIndex}"


def initClumps(totalClumps: int, i: int):
    right_or_left = ["right", "left"]
    actions = ["right", "left", "hop"]
    # clump_check = lambda :
    return [
        randAction("ifenemy", totalClumps, 5, i),
        randAction("ifsame", totalClumps, 7, i),
        randAction("ifwall", totalClumps, 9, i),
        randAction("ifempty", totalClumps, 11, i),
        randAction("infect", totalClumps, 1, i),
        randAction("go", totalClumps, 1, i),
        right_or_left[random.randint(0, 1)],
        randAction("go", totalClumps, 1, i),
        right_or_left[random.randint(0, 1)],
        randAction("go", totalClumps, 1, i),
        actions[random.randint(0, 2)],
        randAction("go", totalClumps, 1, i)
    ]


# This writes a random starting code (that works)
# To evo's procedure file
def writeRandom():
    f = open("texts/oliver.txt", "w")
    # One gene is one chunk, from initClumps
    # During a procedure, when the creature moves
    # To a new step, it will move to the correct step
    # In the same or different clump
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


# This changes one line of the creatures procedure
# And return a new list with the new procedure
# (1 line changed)
# This is what allows the creature to evolve
def mutate(mutation_strength: int):
    def mutation(list1: list):
        for i in range(mutation_strength):
            # Option = 0 means changing the action
            # Option = 1 means changing where the action goes after being executed
            option = random.randint(0, 1)
            # Which chunk will have one line changed
            whichGene = random.randint(0, 49)
            if option:
                # Which action within that chunk will be changed
                whichAction = [7, 9, 11][random.randint(0, 2)]
                # Index of the action to be changed
                index = whichGene * 12 + whichAction - 1
                # Left or right
                if whichAction != 11:
                    list1[index] = "right" if list1[index] == "left" else "left"
                # Hop, left or right
                else:
                    list1[index] = ["right", "left"][random.randint(
                        0, 1)] if list1[index] == "hop" else ["right", "hop"][
                            random.randint(0, 1)] if list1[index] == "left" else [
                                "left", "hop"
                            ][random.randint(0, 1)]
            # Changes the number that an action (that goes
            # to another step) goes to
            # Example: ifwall 1 --> ifwall 13
            else:
                whichAction = [6, 8, 10, 12][random.randint(0, 3)]
                index = whichGene * 12 + whichAction - 1
                newGoIndex = random.randint(0, 49) * 12 + 1
                while newGoIndex == int(list1[index].split()[1]):
                    newGoIndex = random.randint(0, 49) * 12 + 1
                list1[index] = f"go {newGoIndex}"
        return list1
    return mutation
