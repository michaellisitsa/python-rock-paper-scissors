from abc import ABC, abstractmethod
import math
class Object(ABC):
    type: str
    kills: str
    eatenBy: str
    def __init__(self, x: float,y: float):
        self.x = x
        self.y = y
        self.direction = [1,0]

    def get_direction_magnitude(self):
        return math.sqrt(self.direction[0]**2 + self.direction[1]**2)


    def move_in_direction(self, steps: float = 1.):
        dx = steps * self.direction[0] / self.get_direction_magnitude()
        dy = steps * self.direction[1] / self.get_direction_magnitude()
        self.updatePosition(dx, dy)
        
        
    def updatePosition(self, dx:float, dy:float):
        self.x += dx
        self.y += dy
