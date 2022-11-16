from creature1 import Creature
import pygame

#See "rover" or "Oliver" for more explanations
class Flytrap(Creature):
  def __init__(self, x, y, startingDirection):
    super().__init__(x, y, startingDirection)
    self.creatureType = 0
    self.images = [pygame.image.load("resources/flytrap_left.png").convert_alpha(), pygame.image.load("resources/flytrap_down.png").convert_alpha(),pygame.image.load("resources/flytrap_right.png").convert_alpha() , pygame.image.load("resources/flytrap_up.png").convert_alpha()]
    self.image = self.images[self.direct]
    self.actions = ["ifenemy 4", "left", "go 1", "infect 0", "go 1"]
    self.action = self.takeAction
    self.num = 0

  def __str__(self) -> str:
    return "Flytrap"