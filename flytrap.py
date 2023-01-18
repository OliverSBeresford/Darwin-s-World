from creature1 import Creature
import pygame


#The "Flytrap" Creature subtype
class Flytrap(Creature):
    actions = []

    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        #Images used to display it
        self.images = [pygame.image.load("resources/flytrap_up.png").convert_alpha(),
            pygame.image.load("resources/flytrap_right.png").convert_alpha(),
            pygame.image.load("resources/flytrap_down.png").convert_alpha(),
            pygame.image.load("resources/flytrap_left.png").convert_alpha()
        ]
        self.image = self.images[self.direct]
        self.actions = []
        self.initActions()
        self.action = self.takeAction
        self.num = 0

    def __str__(self) -> str:
        return "Flytrap"

    # Puts actions into "self.actions"
    def initActions(self):
        self.actions = []
        # If quick actions access is empty, reads actions file (this case would be trained Oliver class)
        # ("developedCreature.txt")
        # then writes them to the class for future objects
        if not Flytrap.actions:
            file = open("texts/flytrap.txt", "r")
            for line in file:
                self.actions.append(line.strip())
            Flytrap.actions = self.actions.copy()
        else:
            self.actions = Flytrap.actions.copy()
