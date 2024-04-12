import math

from game_mechanics.Position import Position

class Entity:
    def __init__(self, statistics = None, position = Position(200, 200)):
        self.statistics = statistics
        self.position = position

    def move(self, move_vector:Position):
        move_vector.normalized()
        move_vector *= self.statistics.speed
        self.position += move_vector