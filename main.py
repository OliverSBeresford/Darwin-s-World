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
            if time.time() - start >= 2:
                return "tie"
        simulation.darwinUpdate()
    return type(simulation.creatures[0])


# This runs the simulation "times" times and return a dictionary
# Format: {class1: numWins, class2: numWins}
def runXTimes(class1, class2, times, rows=False, creatures=10, mutation=None, epoch=None):
    dict = {class1: 0, class2: 0}
    winner = 0
    for i in range(times):
        os.system("clear")
        if mutation != None and epoch != None:
            print(f"Mutation {mutation} of epoch {epoch} {math.floor(i / times * 100)} % complete...")
        else:
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
            winners = runXTimes(class1, class2, rounds, rows, creatures, i, j)
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

def get_int(prompt):
    valid = False
    while not valid:
        try:
            result = int(input(prompt))
            valid = True
        except:
            valid = False
    return result

def main():
    pygame.init()

    # This is where you choose which classes to use
    class1 = Rover
    class2 = Flytrap
    
    if class1 == Evo or class2 == Evo and int(input("Are you training the evo class? yes = 1, no = 0\n>>")):
        epochs = get_int("How many epochs? More epochs generally means a more highly adapted creature. There is no overfitting.\n>>")
        mutations = get_int("How many mutations? More mutations allows us to test more different mutation sets per epoch but will make the process longer.\n>>")
        rounds = get_int("How many rounds per mutation? More rounds means each mutation will be more thoroughly tested.\n>>")
        rows = get_int("How many rows?\n>>")
        creatures = get_int("How many creatures per species?\n>>")
        print(trainCreature(class1, class2, epochs, mutations, rounds, rows, creatures))
        return

    run = bool(get_int(
                "Would you like to see the simulation or the results? -> 1/0\n>>"
    ))
    
    times = 1 if run else get_int("How many times would you like the program to run?\n->>")
    rows = 15
    if not run:
        rows = get_int("Choose the amount of rows and columns for the execution\n>>")
        creatures = get_int("How many creatures do you want on each side?\n>>")
    Spiral.rows = rows

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
