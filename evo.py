from creature1 import Creature
import random
import pygame
import writerandom


# Rover creature type
class Evo(Creature):
    startup = writerandom.writeRandom
    mutate = writerandom.mutate
    originalActions = startup()
    currentActions = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.images = [
            pygame.image.load("resources/evo_up.png").convert_alpha(),
            pygame.image.load("resources/evo_right.png").convert_alpha(),
            pygame.image.load("resources/evo_down.png").convert_alpha(),
            pygame.image.load("resources/evo_left.png").convert_alpha()
        ]
        self.image = self.images[self.direct]
        self.action = self.takeAction
        self.num = 0
        self.actions = []
        self.initActions()

    def __str__(self) -> str:
        return "Evo"

    def initActions(self):
        self.actions = []
        if not Evo.currentActions:
            self.actions = Evo.mutate(Evo.originalActions)
            Evo.currentActions = self.actions
        else:
            self.actions = Evo.currentActions
