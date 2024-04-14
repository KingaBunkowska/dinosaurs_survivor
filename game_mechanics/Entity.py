import math

from game_mechanics.Position import Position

class Entity:
    def __init__(self, statistics = None, position = Position(200, 200)):
        self.statistics = statistics
        self.position = position
        self.hitbox = (self.position.x + 20, self.position.y, 28, 60)

    def move(self, move_vector:Position):
        move_vector.normalized()
        move_vector *= self.statistics.speed
        self.position += move_vector
    def hit(self, projectile):
        if (self != projectile.caster):
            skip