from creature1 import Creature
#from flytrap import Flytrap
import pygame

#Rover creature type
class Rover(Creature):
  #Inherits Creature's initialization function and adds 2 new features
  def __init__(self, x, y, startingDirection):
    super().__init__(x, y, startingDirection)
    self.creatureType = 1
    self.images = [pygame.image.load("resources/rover_left.png").convert_alpha(), pygame.image.load("resources/rover_down.png").convert_alpha(),pygame.image.load("resources/rover_right.png").convert_alpha() , pygame.image.load("resources/rover_up.png").convert_alpha()]
    self.image = self.images[self.direct]
    self.actions = [[self.ifEnemyN,11],[self.ifWallN,6],[self.ifSameN,6],[self.hop], [self.go,1],[self.ifRandomN, 9],[self.right],[self.go,1], [self.left], [self.go,1], [self.infectN, 0],[self.go,1]]
    self.action = self.takeAction
    self.num = 0

  def __str__(self) -> str:
    return "Rover"
    

  