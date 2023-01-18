from creature1 import Creature
import pygame
import math


# Spiral creature subtype
# Spirals into the middle, goes back out and repeats
class Spiral(Creature):
    actionsForAll = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        #Spiral's images
        self.images = [
            pygame.image.load("resources/spiral_up.png").convert_alpha(),
            pygame.image.load("resources/spiral_right.png").convert_alpha(),
            pygame.image.load("resources/spiral_down.png").convert_alpha(),
            pygame.image.load("resources/spiral_left.png").convert_alpha()
        ]
        # Current image
        self.image = self.images[self.direct]
        self.action = self.takeAction
        self.num = 0
        self.actions = []
        # Writes all actions to file if the list of actions for all spirals is empty
        # Otherwise reads the actionsForAll to get its actions
        self.initActions()

    def __str__(self) -> str:
        return "Spiral"

    # Very very complicated, but in short:
    # Function to write all actions to the file with the actions
    # Will needs to have different actions each time because
    # Spiral's procedure depends on cols and rows
    def writeProcedure(self):
        boardSize = Spiral.rows
        getClump = lambda string1, string2, num: ("ifenemy " + str(
            (num - 1) * 9 + 8
        ), "ifwall 1", "ifsame " + str(num * 9 + 6), string1, "go " + str(
            num * 9 + 1), string2, "go " + str(num * 9 + 1), 'infect ' + str(
                num * 9 + 1), "go " + str(num * 9 + 1))

        def repeat(times, total, file):
            for i in range(times):
                for line in getClump("hop", "right", total):
                    file.write(line + "\n")
                total += 1
            return total

        def turnRight(f, num):
            for k in getClump("right", 'right', num):
                if k != "ifwall 1":
                    f.write(k + "\n")
                else:
                    f.write("ifwall " + str((num - 1) * 9 + 6) + "\n")
            return num + 1

        # These starting commands lead the creature to
        # a wall, facing the right direction to start
        file = open("texts/spiral.txt", "w")
        totalTimes = 4
        for i in ("ifenemy 8", "ifwall 10", "ifsame 6", "hop", "go 1", "right",
                  "go 1", 'infect 1', "go 1"):
            file.write(i + "\n")
        for i in ("ifenemy 17", "ifwall 15", "ifsame 15", "right", "go 1",
                  "right", "go 19", 'infect 1', "go 10"):
            file.write(i + "\n")
        for i in ("ifenemy 26", "ifwall 28", "ifsame 1", "hop", "go 19",
                  "right", "go 19", 'infect 1', "go 19"):
            file.write(i + "\n")

        # This write the creature's spiral mechanism
        for i in range(math.ceil(boardSize / 2)):
            totalTimes = turnRight(file, totalTimes)
            totalTimes = repeat(boardSize -
                                1, totalTimes, file) if not i else repeat(
                                    boardSize - i * 2, totalTimes, file)
            for _ in range(2):
                totalTimes = turnRight(file, totalTimes)
                totalTimes = repeat(boardSize - i * 2 - 1, totalTimes, file)
            totalTimes = turnRight(file, totalTimes)
            totalTimes = repeat(boardSize - i * 2 - 2, totalTimes, file)
        file.write("go 37")
        file.close()

    # Initializes the creature's actions
    def initActions(self):
        self.actions = []
        # If quick action getting is empty, creates actions
        if not Spiral.actionsForAll:
            self.writeProcedure()
            f = open("texts/spiral.txt", "r")
            for line in f:
                self.actions.append(line.strip())
            f.close()
            # Writes actions to the class to be used for all future objects
            Spiral.actionsForAll = self.actions
        else:
            self.actions = Spiral.actionsForAll
