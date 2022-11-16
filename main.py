import sys, os, time
import pygame
from flytrap import Flytrap
from oliver import Oliver
from rover import Rover
from darwin import Darwin
import math
from trained import Trained
from spiral import Spiral


# The program was working perfectly before, but now that I have started to make it more versatile so that I can make the "Oliver" class have completely random actions it has come up with some minor issues


# This function runs the simulation once, takes the creature classes and whether you want to see the simulation as parameters
def runSimulation(class1, class2, simOrNo, rows=False, creatures=10):
    start = time.time()
    simulation = Darwin(class1, class2, simOrNo, rows, creatures)
    simulation.setup()
    # This draws everything

    while not simulation.isOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not simOrNo:
            if time.time() - start >= 5:
                print("One round timed out (tie).")
                return "tie"
        simulation.darwinUpdate()
    return type(simulation.creatures[0])


def runXTimes(class1, class2, simOrNo, times, rows=False, creatures=10):
    dict = {class1: 0, class2: 0}
    winner = 0
    for i in range(times):
        os.system("clear")
        print(f"{math.floor(i / times * 100)} % complete...")
        ties = 0
        winner = runSimulation(class1, class2, False, rows, creatures)
        while winner == "tie":
            winner = runSimulation(class1, class2, False, rows, creatures)
            ties += 1
            if ties >= 5:
                print("Timed out because of a tie. Most likely the way the creatures are made prevents them from making contact with each other. GG")
        dict[winner] += 1
    return dict


def trainCreature(class1, class2, rows=False, creatures=10):
    file = open("texts/originalCreature.txt", "w")
    for line in class1.originalActions:
        file.write(line + "\n")
    file.write("go 1")
    file.close()
    for i in range(50):
        maxWins = 0
        bestProcedure = []
        for j in range(32):
            class1.currentActions = []
            winners = runXTimes(class1, class2, False, 5, rows, creatures)
            if winners[class1] > maxWins:
                maxWins = winners[class1]
                bestProcedure = Oliver.currentActions.copy()
        class1.originalActions = bestProcedure.copy()
    file = open("texts/developedCreature.txt", "w")
    for line in class1.originalActions:
        file.write(line + "\n")
    file.write("go 1")
    file.close()
    return "Complete"


def main():
    try:
        run = bool(int(input("Would you like to see the simulation or the results? -> 1/0\n>>")))
    except:
        print("I said 1/0")
    times = 1 if run else int(
        input("How many times would you like the program to run?\n->>"))
    if not run:
        rows = int(input("Choose the amount of rows and columns for the execution\n>>"))
        creatures = int(input("How many creatures do you want on each side?\n>>"))
    pygame.init()
    pygame.display.set_caption('Darwin\'s World')

    # I couldn't figure out how to get rid of the icon that was on top of "Darwin's World" so I just did this
    x = pygame.Surface((0, 0))
    pygame.display.set_icon(x)
    os.system("clear")
    # here is where you choose which classes to use, you send 2 classes as parameters for the runSimulation function
    class1 = Spiral
    class2 = Flytrap
    if run:
        print(str(runSimulation(class1, class2, True)(1, 2, 3)), "wins!")
    else:
        os.system("clear")
        if int(input("Are you testing the oliver class? yes = 1, no = 0\n>>")):
            print("testing...")
            print(trainCreature(class1, class2, rows, creatures))
        else:
            os.system("clear")
            dict = runXTimes(class1, class2, False, times, rows, creatures)
            print("100 % complete.")
            print(str(class1(1, 2, 3)), ":", dict[class1] / times * 100, "%")
            print(str(class2(1, 2, 3)), ":", dict[class2] / times * 100, "%")


# Rover: about 74% win rate, Flytrap: about 26% win rate
if __name__ == "__main__":
    main()

# ignore this. for more info on this strange occurance go to creature1 :)
# right -> down, up -> left, left -> up, down -> right???
