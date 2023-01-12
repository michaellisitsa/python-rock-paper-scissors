from Game.Object import Object

class Scissors(Object):
    type="scissors"
    beats="paper"
    beaten_by="rock"
    def __init__(self, x:float, y: float):
        super().__init__(x,y)

    def updatePosition(self, dx:float, dy:float):
        self.x += dx
        self.y += dy


