from abc import ABC, abstractmethod

class Object(ABC):
    type: str
    kills: str
    eatenBy: str
    def __init__(self, x: float,y: float):
        self.x = x
        self.y = y
        
    @abstractmethod
    def updatePosition(self, dx:float, dy:float):
        pass
