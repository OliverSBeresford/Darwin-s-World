from creature1 import Creature
# from flytrap import Flytrap
import pygame


# Rover creature type
class Rover(Creature):
    # Inherits Creature's initialization function and adds 2 new features
    def __init__(self, x, y, startingDirection):
        super().__init__(x, y, startingDirection)
        self.creatureType = 1
        self.images = [pygame.image.load("resources/rover_left.png").convert_alpha(),
                       pygame.image.load("resources/rover_down.png").convert_alpha(),
                       pygame.image.load("resources/rover_right.png").convert_alpha(),
                       pygame.image.load("resources/rover_up.png").convert_alpha()]
        self.image = self.images[self.direct]
        self.actions = ["ifenemy 11", "ifwall 6", "ifsame 6", "hop", "go 1", "ifrandom 9", "right", "go 1", "left", "go 1", "infect 0", "go 1"]
        self.action = self.takeAction
        self.num = 0

    def __str__(self) -> str:
        return "Rover"


