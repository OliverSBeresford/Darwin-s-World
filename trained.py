from creature1 import Creature
import random
import pygame
import writerandom


# Rover creature type
class Trained(Creature):
    actions = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.images = [pygame.image.load("resources/oli_left.png").convert_alpha(),
                       pygame.image.load("resources/oli_down.png").convert_alpha(),
                       pygame.image.load("resources/oli_right.png").convert_alpha(),
                       pygame.image.load("resources/oli_up.png").convert_alpha()]
        self.image = self.images[self.direct]
        self.action = self.takeAction
        self.num = 0
        self.actions = []
        self.initActions()

    def __str__(self) -> str:
        return "Trained"

    def initActions(self):
        self.actions = []
        if not Trained.actions:
            file = open("texts/developedCreature.txt", "r")
            for line in file:
                self.actions.append(line)
            Trained.actions = self.actions.copy()
        else:
            self.actions = Trained.actions.copy()
