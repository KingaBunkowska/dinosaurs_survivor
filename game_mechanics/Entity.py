import math

from game_mechanics.Position import Position

class Entity:
    def __init__(self, statistics = None, position = Position(200, 200)):
        self.statistics = statistics
        self.position = position

        self.hitbox = (self.position.x + 20, self.position.y, 28, 60)
        self.facing_right = False


    def move(self, move_vector:Position):
        move_vector.normalized()
        move_vector *= self.statistics.speed
        self.position += move_vector
        
    def hit(self, projectile):
        if (self != projectile.caster):
            skip

        self.position += move_vector
        
        if move_vector.to_coords()[0] > 10**-3:
            self.facing_right = True
        else:
            self.facing_right = False
        
    def get_position(self):
        return self.position

