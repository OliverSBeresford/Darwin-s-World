# This class is inherited by each sub-creature type, so the times that this calls a function not in this class, it is probably part of the sub-creature's class
import random


class Creature:
    def __init__(self, x, y, startingDirection):
        self.pos = [x, y]
        self.direct = startingDirection
        # self.currentAction = self.firstAction()

    # A setter method to set direction (useful because it also changes image)
    def setDirect(self, newValue):
        self.direct = newValue
        self.image = self.images[self.direct]

    # Checks if there is a world border ahead
    def wallInFront(self, game):
        if self.direct == 0:
            if self.pos[1] == 0:
                return True
            return False
        elif self.direct == 1:
            if self.pos[0] >= game.ROWS - 1:
                return True
            return False
        elif self.direct == 2:
            if self.pos[1] >= game.ROWS - 1:
                return True
            return False
        else:
            if self.pos[0] == 0:
                return True
            return False

    # Moves one box forward
    def hop(self, game):
        if self.wallInFront(game):
            return
        if self.direct == 0:
            self.pos[1] -= 1
        elif self.direct == 1:
            self.pos[0] += 1
        elif self.direct == 2:
            self.pos[1] += 1
        else:
            self.pos[0] -= 1
        for i in game.creatures:
            game.board[i.pos[1]][i.pos[0]] = i

    # The directions work, but something a little weird is going on. This seems like it is turning right (0 is up 1 is right 2 is down 3 is left), but it is actually left... Also, the directions lists are really weird and still somehow work. When direction is 0, all the calculations calulate as though it were facing up, and yet subCreature.images[0] is the LEFT facing photo, and still somehow everything works... Left is switched with up and right is switched with down.
    def left(self, game):
        self.setDirect(0) if self.direct == 3 else self.setDirect(self.direct + 1)

    def right(self, game):
        self.setDirect(3) if self.direct == 0 else self.setDirect(self.direct - 1)

    # Checks if the box in front is unoccupied
    def emptyInFront(self, game):
        if self.wallInFront(game):
            return False
        if self.direct == 0:
            if not game.board[self.pos[1] - 1][self.pos[0]]:
                return True
            return False
        elif self.direct == 1:
            if not game.board[self.pos[1]][self.pos[0] + 1]:
                return True
            return False
        elif self.direct == 2:
            if not game.board[self.pos[1] + 1][self.pos[0]]:
                return True
            return False
        else:
            if not game.board[self.pos[1]][self.pos[0] - 1]:
                return True
            return False

    # Method checks whether the piece in front of a creature is of the same creature type
    def ifSame(self, game):
        if self.wallInFront(game):
            return
        if self.ifEnemy(game):
            return False
        elif self.emptyInFront(game):
            return False
        return True

    def infectN(self, creature, game, n):
        if self.wallInFront(game):
            return
        game.creatures.remove(creature)
        newc = type(self)(creature.pos[0], creature.pos[1], creature.direct)
        newc.num = n
        game.creatures.append(newc)
        for i in game.creatures:
            game.board[i.pos[1]][i.pos[0]] = i
        if game.isSimulationOver():
            game.isOver = True

    def ifEnemy(self, game):
        if self.wallInFront(game):
            return False
        if self.direct == 0:
            if not self.emptyInFront(game) and type(game.board[self.pos[1] - 1][self.pos[0]]) != type(self):
                return game.board[self.pos[1] - 1][self.pos[0]]
            return False
        elif self.direct == 1:
            if not self.emptyInFront(game) and type(game.board[self.pos[1]][self.pos[0] + 1]) != type(self):
                return game.board[self.pos[1]][self.pos[0] + 1]
            return False
        elif self.direct == 2:
            if not self.emptyInFront(game) and type(game.board[self.pos[1] + 1][self.pos[0]]) != type(self):
                return game.board[self.pos[1] + 1][self.pos[0]]
            return False
        else:
            if not self.emptyInFront(game) and type(game.board[self.pos[1]][self.pos[0] - 1]) != type(self):
                return game.board[self.pos[1]][self.pos[0] - 1]
            return False


    def takeAction(self, game, num):
        self.num = num
        action = self.actions[self.num - 1].split()
        if len(action) - 1:
            action[1] = int(action[1])
            if action[0] == "go":
                self.go(game, action[1])
            elif action[0] == "ifenemy":
                self.ifEnemyN(game, action[1])
            elif action[0] == "ifwall":
                self.ifWallN(game, action[1])
            elif action[0] == "ifsame":
                self.ifSameN(game, action[1])
            elif action[0] == "ifempty":
                self.ifEmptyN(game, action[1])
            elif action[0] == "infect":
                self.infectN(self.ifEnemy(game), game, action[1])
            elif action[0] == "ifrandom":
                self.ifRandomN(game, action[1])
        else:
            if action[0] == "right":
                self.right(game)
            elif action[0] == "left":
                self.left(game)
            elif action[0] == "hop":
                self.hop(game)

    def go(self, game, num):
        self.takeAction(game, num)

    def ifWallN(self, game, n):
        if self.wallInFront(game):
            self.takeAction(game, n)
        else:
            self.takeAction(game, self.num + 1)

    def ifEnemyN(self, game, n):
        if self.ifEnemy(game):
            self.takeAction(game, n)
        else:
            self.takeAction(game, self.num + 1)

    def ifSameN(self, game, n):
        if self.ifSame(game):
            self.takeAction(game, n)
        else:
            self.takeAction(game, self.num + 1)

    def ifEmptyN(self, game, n):
        if self.emptyInFront(game):
            self.takeAction(game, n)
        else:
            self.takeAction(game, self.num + 1)

    def ifRandomN(self, game, n):
        if random.randint(0, 1):
            self.takeAction(game, n)
        self.takeAction(game, self.num + 1)



