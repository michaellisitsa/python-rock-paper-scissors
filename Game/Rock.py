from Game.Object import Object

class Rock(Object):
    type="rock"
    beats="scissors"
    beaten_by="paper"
    def __init__(self, x:float, y: float):
        super().__init__(x,y)

    def updatePosition(self, dx:float, dy:float):
        self.x += dx
        self.y += dy



