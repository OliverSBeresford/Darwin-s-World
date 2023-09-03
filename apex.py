from creature1 import Creature
import pygame

# Rover creature type
class Apex(Creature):
    actions = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.creatureType = 1
        self.images = [
            pygame.image.load("resources/apex_up.png"),
            pygame.image.load("resources/apex_right.png"),
            pygame.image.load("resources/apex_down.png"),
            pygame.image.load("resources/apex_left.png")
        ]
        self.image = self.images[self.direct]
        self.actions = []
        self.initActions()
        self.action = self.takeAction
        self.num = 0

    def __str__(self) -> str:
        return "Apex"

    # Puts actions into "self.actions"
    def initActions(self):
        self.actions = []
        # If quick actions access is empty, reads actions file
        # then writes them to the class for future objects
        if not Apex.actions:
            file = open("texts/apex.txt", "r")
            for line in file:
                self.actions.append(line.strip())
            Apex.actions = self.actions.copy()
        else:
            self.actions = Apex.actions.copy()
