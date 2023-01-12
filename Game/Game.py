from Game.Rock import Rock
from Game.Scissors import Scissors
from Game.Paper import Paper
from Game.Object import Object

class Game():
    def __init__(self):
        self.list: list[Object] = []

    def create_object(self, type: str, x: float = 0, y: float = 0):
        if type == Rock.type:
            self.list.append(Rock(x,y))
        elif type == Scissors.type:
            self.list.append(Scissors(x,y))
        elif type == Paper.type:
            self.list.append(Paper(x,y))
        else:
            print("Cannot create type: ", type)


    def add_object(self, object: Rock | Scissors):
        self.list.append(object)
