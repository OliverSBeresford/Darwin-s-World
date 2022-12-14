from creature1 import Creature
import random
import pygame
import writerandom


# Rover creature type
class Oliver(Creature):
    startup = writerandom.writeRandom
    mutate = writerandom.mutate
    originalActions = startup()
    currentActions = []

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
        return "Oliver"

    def initActions(self):
        self.actions = []
        if not Oliver.currentActions:
            self.actions = Oliver.mutate(Oliver.originalActions)
            Oliver.currentActions = self.actions
        else:
            self.actions = Oliver.currentActions
