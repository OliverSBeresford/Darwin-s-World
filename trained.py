from creature1 import Creature
import random
import pygame
import writerandom


# Trained creature type
# This creature is the trained creature (oliver is the training class)
# To use, use oliver creature class ("class1" on main becomes Oliver
# "Class2" is what you're training "Oliver" against
# follow instructions (say 1 to "are you training the oliver class")
# Switch to trained (edit "class1" to be Trained)
class Trained(Creature):
    actions = []

    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.images = [
            pygame.image.load("resources/trained_up.png"),
            pygame.image.load("resources/trained_right.png"),
            pygame.image.load("resources/trained_down.png"),
            pygame.image.load("resources/trained_left.png")
        ]
        self.image = self.images[self.direct]
        self.action = self.takeAction
        self.num = 0
        self.actions = []
        # Puts procedure into "self.actions"
        self.initActions()

    # Used to print out a Trained object
    def __str__(self) -> str:
        return "Trained"

    # Puts actions into "self.actions"
    def initActions(self):
        self.actions = []
        # If quick actions access is empty, reads actions file (this case would be trained Oliver class)
        # ("developedCreature.txt")
        # then writes them to the class for future objects
        if not Trained.actions:
            file = open("texts/developedCreature.txt", "r")
            for line in file:
                self.actions.append(line.strip())
            Trained.actions = self.actions.copy()
        else:
            self.actions = Trained.actions.copy()
