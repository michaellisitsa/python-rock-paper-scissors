from Game.Object import Object

class Paper(Object):
    type="paper"
    beats="rock"
    beaten_by="scissors"
    def __init__(self, x:float, y: float):
        super().__init__(x,y)



