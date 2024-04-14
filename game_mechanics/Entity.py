import math

from game_mechanics.Position import Position

class Entity:
    def __init__(self, statistics = None, position = Position(200, 200)):
        self.statistics = statistics
        self.position = position
        self.facing_right = False

    def move(self, move_vector:Position):
        move_vector.normalized()
        move_vector *= self.statistics.speed
        self.position += move_vector
        if move_vector.to_coords()[0] > 0:
            self.facing_right = True
        else:
            self.facing_right = False
    
    def get_position(self):
        return self.position