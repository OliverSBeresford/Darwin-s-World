from creature1 import Creature
import pygame
import math


# Rover creature type
class Spiral(Creature):
    actionsForAll = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.images = (pygame.image.load("resources/oli_left.png").convert_alpha(),
                       pygame.image.load("resources/oli_down.png").convert_alpha(),
                       pygame.image.load("resources/oli_right.png").convert_alpha(),
                       pygame.image.load("resources/oli_up.png").convert_alpha())
        self.image = self.images[self.direct]
        self.action = self.takeAction
        self.num = 0
        self.actions = []
        self.initActions()

    def __str__(self) -> str:
        return "Spiral"

    def writeProcedure(self):
        boardSize = int(input("what's the board size again? \n>>"))
        getClump = lambda string1, string2, num: ("ifenemy " + str((num - 1) * 9 + 8),
                                                  "ifwall 1",
                                                  "ifsame " + str(num * 9 + 6),
                                                  string1,
                                                  "go " + str(num * 9 + 1),
                                                  string2,
                                                  "go " + str(num * 9 + 1),
                                                  'infect ' + str(num * 9 + 1),
                                                  "go " + str(num * 9 + 1))

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
                    f.write("ifwall " + str((num-1) * 9 + 6) + "\n")
            return num + 1

        file = open("texts/spiral.txt", "w")
        '''for i in ("ifenemy 8", "ifwall 10", "ifsame 6", "hop", "go 1", "right", "go 1", 'infect 1', "go 1"):
            file.write(i + "\n")
        for i in ("ifenemy 17", "ifwall 15", "ifsame 15", "right", "go 1", "right", "go 19", 'infect 1', "go 10"):
            file.write(i+ "\n")
        for i in ("ifenemy 26", "ifwall 28", "ifsame 1", "hop", "go 19", "right", "go 19", 'infect 1', "go 19"):
            file.write(i + "\n")'''
        totalTimes = 4
        for i in ("ifenemy 8", "ifwall 10", "ifsame 6", "hop", "go 1", "right", "go 1", 'infect 1', "go 1"):
            file.write(i + "\n")
        for i in ("ifenemy 17", "ifwall 15", "ifsame 15", "right", "go 1", "right", "go 19", 'infect 1', "go 10"):
            file.write(i + "\n")
        for i in ("ifenemy 26", "ifwall 28", "ifsame 1", "hop", "go 19", "right", "go 19", 'infect 1', "go 19"):
            file.write(i + "\n")
        '''for i in ("ifenemy 35", "ifwall 33", "ifsame 33", "right", "go 37", "right", "go 37", 'infect 1', "go 37"):
            file.write(i + "\n")'''
        '''totaltimes = repeat(3, totaltimes, file, "hop")
        totaltimes = repeat(2, totaltimes, file, "right")'''
        for i in range(math.ceil(boardSize / 2)):
            totalTimes = turnRight(file, totalTimes)
            totalTimes = repeat(boardSize - 1, totalTimes, file) if not i else repeat(boardSize - i * 2, totalTimes,
                                                                                      file)
            for _ in range(2):
                totalTimes = turnRight(file, totalTimes)
                totalTimes = repeat(boardSize - i * 2 - 1, totalTimes, file)
            totalTimes = turnRight(file, totalTimes)
            totalTimes = repeat(boardSize - i * 2 - 2, totalTimes, file)
        file.write("go 37")
        file.close()

    def initActions(self):
        self.actions = []
        if not Spiral.actionsForAll:
            self.writeProcedure()
            f = open("texts/spiral.txt", "r")
            for line in f:
                self.actions.append(line)
            f.close()
            Spiral.actionsForAll = self.actions
        else:
            self.actions = Spiral.actionsForAll
