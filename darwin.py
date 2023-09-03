import time
import random
import pygame
import math


#The "Darwin" class, this has all the functions needed
#to actually run the game
class Darwin:

    def __init__(self, firstClass, secondClass, simOrNo, rows,
                 amountOfCreatures):
        #Inits the pygame screen
        self.WIDTH = 300
        self.HEIGHT = 300
        self.ROWS = rows if rows else 15
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        #Starts seting up board
        self.board = [[0] * 15 for x in range(15)]
        self.creatures = []
        self.isOver = False
        #Simulation viewable or not
        self.sim = simOrNo
        #Used to make sure creatures don't spawn on each other
        self.positions = []
        #Takes in classes that are being used for this round
        self.class1 = firstClass
        self.class2 = secondClass
        self.amCr = amountOfCreatures

    #Method that makes each creature take a turn, then prints it
    def darwinUpdate(self):
        #Reset "true" board (creature object for creature, 0 for empty)
        self.board = [[0] * self.ROWS for x in range(self.ROWS)]

        for i in self.creatures:
            self.board[i.pos[1]][i.pos[0]] = i

        # The order of the creatures' turns is the same as the order that they
        # Are in in the list where they are sorted\
        # Which has a format of: [random of class1, random of class2, random of class1...]
        for i in range(len(self.creatures)):
            #Creature takes its turn
            self.creatures[i].action(self, self.creatures[i].num + 1)
            #resetting board
            self.board = [[0] * self.ROWS for x in range(self.ROWS)]
            for k in self.creatures:
                self.board[k.pos[1]][k.pos[0]] = k
            # Displays the board, then sleeps for 0.05 seconds
            # (Quite fast because a frame is when one out of 20 creatures moves)
            if self.sim:
                self.updateBoard(self.creatures[i])
                # Change this to make it faster or slower
                time.sleep(0.05)

    #Updates screen
    def updateBoard(self, creature):
        #Erases everything on screen, replaces it with White
        self.screen.fill((255, 255, 255))
        #Puts grid onto screen
        self.draw(self.HEIGHT / self.ROWS, self.WIDTH / self.ROWS)
        #Draws all creatures
        for i, newList in enumerate(self.board):
            for j, value in enumerate(newList):
                if self.board[i][j]:
                    self.screen.blit(value.image, (j * 20, i * 20))
        #Actually displays the screen
        pygame.display.flip()

    #Return true if all creatures are of one type, so the simulation is over
    #That type has won
    def isSimulationOver(self):
        x = self.creatures[0]
        for i in self.creatures:
            if type(i) != type(x):
                return False
        return True

    #Puts all creatures onto the board (starting setup), random coordinates and direction
    def setup(self):
        #Number of creatures per team
        num = self.amCr if (self.amCr * 2) <= (self.ROWS * self.ROWS) else int(
            math.floor(float(self.ROWS) * 4 / 3 / 2))

        randomX = random.randint(0, self.ROWS - 1)
        randomY = random.randint(0, self.ROWS - 1)
        #Creatures at random locations with random directions onto board
        for i in range(num):
            while (randomX, randomY) in self.positions:
                randomX = random.randint(0, self.ROWS - 1)
                randomY = random.randint(0, self.ROWS - 1)
            self.positions.append((randomX, randomY))
            self.creatures.append(
                self.class1(randomX, randomY, random.randint(0, 3)))
            while (randomX, randomY) in self.positions:
                randomX = random.randint(0, self.ROWS - 1)
                randomY = random.randint(0, self.ROWS - 1)
            self.positions.append((randomX, randomY))
            self.creatures.append(
                self.class2(randomX, randomY, random.randint(0, 3)))

    #This draws the grid on the screen
    def draw(self, boxHeight, boxWidth):
        x = 0
        y = 0
        self.screen.fill((255, 255, 255))
        for i in range(self.ROWS):
            x += boxWidth
            y += boxHeight
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.WIDTH))
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.WIDTH, y))
