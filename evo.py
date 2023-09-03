from creature1 import Creature
import random
import pygame
import writerandom


# Rover creature type
class Evo(Creature):
    startup = writerandom.writeRandom
    mutate = None
    originalActions = startup()
    currentActions = []
    mutation_strength = None

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.images = [
            pygame.image.load("resources/evo_up.png"),
            pygame.image.load("resources/evo_right.png"),
            pygame.image.load("resources/evo_down.png"),
            pygame.image.load("resources/evo_left.png")
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
            if not Evo.mutation_strength:
                Evo.mutation_strength = int(input("How much would you like the creature to mutate for each mutation set? Higher mutation strength means more randomness for each tested mutation, so sometimes faster training.\n>>"))
                Evo.mutate = writerandom.mutate(Evo.mutation_strength)
            self.actions = Evo.mutate(Evo.originalActions)
            Evo.currentActions = self.actions
        else:
            self.actions = Evo.currentActions
