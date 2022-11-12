from creature1 import Creature
import random
import pygame
import writerandom

#Rover creature type
class Oliver(Creature):
  writerandom= writerandom.writeRandom
  writerandom()
  actionsForAll = []

  #Inherits Creature's initialization function and adds 2 new features
  def __init__(self, x, y, startingDirection):
    super().__init__(x, y, startingDirection)
    self.images = [pygame.image.load("resources/oli_left.png").convert_alpha(), pygame.image.load("resources/oli_down.png").convert_alpha(),pygame.image.load("resources/oli_right.png").convert_alpha() , pygame.image.load("resources/oli_up.png").convert_alpha()]
    self.image = self.images[self.direct]
    self.action = self.takeAction
    self.num = 0
    self.actions = []
    self.initActions()

  def __str__(self) -> str:
    return "Oliver"

  def initActions(self):
    actionDict = {"hop":self.hop, "left":self.left, "right":self.right, "infect":self.infectN, "ifempty":self.ifEmptyN, "ifwall":self.ifWallN, "ifsame":self.ifSameN, "ifenemy":self.ifEnemyN, "ifrandom":self.ifRandomN, "go":self.go}
    self.actions = []
    if Oliver.actionsForAll == []:
      f = open("texts/oliver.txt", "r")
      for line in f:
        newLine = line.strip().split()
        if newLine != []:
          if len(newLine) - 1:
            self.actions.append([actionDict[newLine[0]], int(newLine[1])])
          else:
            if newLine == ["infect"]:
              self.actions.append([actionDict[newLine[0]], 0])
            else:
              self.actions.append([actionDict[newLine[0]]])
          Oliver.actionsForAll.append(newLine)
      f.close()
    else:
      for i in Oliver.actionsForAll:
        if len(i) - 1:
          self.actions.append([actionDict[i[0]], int(i[1])])
        else:
          self.actions.append([actionDict[i[0]]])
        
    
    
    