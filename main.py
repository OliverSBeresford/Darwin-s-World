import sys, os, time
import pygame
from flytrap import Flytrap
from evo import Evo
from rover import Rover
from darwin import Darwin
import math
from trained import Trained
from spiral import Spiral
from apex import Apex

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
        # This is when you aren't seeing the actual simulation
        if not simOrNo:
            # If it's taking too long
            if time.time() - start >= 5:
                return "tie"
        simulation.darwinUpdate()
    return type(simulation.creatures[0])


# This runs the simulation "times" times and return a dictionary
# Format: {class1: numWins, class2: numWins}
def runXTimes(class1, class2, times, rows=False, creatures=10):
    dict = {class1: 0, class2: 0}
    winner = 0
    for i in range(times):
        os.system("clear")
        print(f"{math.floor(i / times * 100)} % complete...")
        winner = runSimulation(class1, class2, False, rows, creatures)
        while winner == "tie":
            winner = runSimulation(class1, class2, False, rows, creatures)
        dict[winner] += 1
        print("100 % complete.")
    return dict


#This is the function to train Evo against a creature
# Class1 is Evo and class2 is what you are training it against
def trainCreature(class1, class2, epochs=50, mutations=32, rounds=5, rows=False, creatures=10):
    file = open("texts/originalCreature.txt", "w")
    for line in Evo.originalActions:
        file.write(line + "\n")
    file.write("go 1")
    file.close()
    # This writes all of Evo's starting actions (not evolved) to a file that won't be changed
    # Doesn't actually do anything in particular, ust to see how it evolved

    # Evolves epochs times, can be changed
    # As it is training, each epoch will print its progress from 0 to 100 %
    for i in range(epochs):
        maxWins = 0
        bestProcedure = []
        # Mutates 32 different times
        for j in range(mutations):
            Evo.currentActions = []
            # With each mutation, tries it 5 times against Class2
            winners = runXTimes(class1, class2, False, rounds, rows, creatures)
            # If this time is the best time out of the 32 so far,
            # writes down that set of actions
            if winners[Evo] > maxWins:
                maxWins = winners[Evo]
                bestProcedure = Evo.currentActions.copy()
        # uses bestProcedure for next round
        Evo.originalActions = bestProcedure.copy()
    # Writes fully evolved fersion to this file (developed Creature)
    file = open("texts/developedCreature.txt", "w")
    for line in Evo.originalActions:
        file.write(line + "\n")
    file.write("go 1")
    file.close()
    return "Complete. You can now use the \"Trained\" class to use the evolved creature."


def main():
    # This is where you choose which classes to use
    class1 = Trained
    class2 = Rover
    
    if int(input("Are you training the evo class? yes = 1, no = 0\n>>")):
        epochs = int(input("How many epochs? More epochs generally means a more highly adapted creature. There is no overfitting.\n>>"))
        mutations = int(input("How many mutations? More mutations allows us to test more different mutation sets per epoch\n>>"))
        rounds = int(input("How many rounds per mutation? More rounds means each mutation will be more thoroughly tested.\n>>"))
        rows = int(input("How many rows?\n>>"))
        creatures = int(input("How many creatures per species?\n>>"))
        print(trainCreature(class1, class2, epochs, mutations, rounds, rows, creatures))
        return

    try:
        run = bool(
            int(
                input(
                    "Would you like to see the simulation or the results? -> 1/0\n>>"
                )))
    except:
        print("I said 1/0")
        return
    times = 1 if run else int(
        input("How many times would you like the program to run?\n->>"))
    rows = 15
    if not run:
        rows = int(
            input(
                "Choose the amount of rows and columns for the execution\n>>"))
        creatures = int(
            input("How many creatures do you want on each side?\n>>"))
    Spiral.rows = rows
    pygame.init()
    pygame.display.set_caption('Darwin\'s World')

    x = pygame.Surface((0, 0))
    pygame.display.set_icon(x)
    os.system("clear")
    # here is where you choose which classes to use, you send 2 classes as parameters for the runSimulation function

    if run:
        print(str(runSimulation(class1, class2, True)(1, 2, 3)), "wins!")
    else:
        os.system("clear")
        dict = runXTimes(class1, class2, times, rows, creatures)
        print(str(class1(1, 2, 3)), ":", dict[class1] / times * 100, "%")
        print(str(class2(1, 2, 3)), ":", dict[class2] / times * 100, "%")


# Rover: about 74% win rate, Flytrap: about 26% win rate
if __name__ == "__main__":
    main()
