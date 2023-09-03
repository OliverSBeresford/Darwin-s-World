from creature1 import Creature
import pygame


# Rover creature type
class Rover(Creature):
    actions = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.creatureType = 1
        self.images = [
            pygame.image.load("resources/rover_up.png"),
            pygame.image.load("resources/rover_right.png"),
            pygame.image.load("resources/rover_down.png"),
            pygame.image.load("resources/rover_left.png")
        ]
        self.image = self.images[self.direct]
        self.actions = []
        self.initActions()
        self.action = self.takeAction
        self.num = 0

    def __str__(self) -> str:
        return "Rover"

    # Puts actions into "self.actions"
    def initActions(self):
        self.actions = []
        # If quick actions access is empty, reads actions file
        # then writes them to the class for future objects
        if not Rover.actions:
            file = open("texts/rover.txt", "r")
            for line in file:
                self.actions.append(line.strip())
            Rover.actions = self.actions.copy()
        else:
            self.actions = Rover.actions.copy()
