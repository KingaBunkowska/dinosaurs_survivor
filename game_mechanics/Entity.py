from game_mechanics.Position import Position

class Entity:
    def __init__(self, statistics = None, position = Position(200, 200), facing_right=False):
        self.statistics = statistics
        self.position = position

        self.original_facing_right = facing_right
        self.facing_right = facing_right


    def move(self, move_vector:Position):
        move_vector.normalized()
        move_vector *= self.statistics.speed
        self.position += move_vector
        
        if move_vector.to_coords()[0] > 10**-3:
            self.facing_right = not self.original_facing_right
        else:
            self.facing_right = self.original_facing_right

        
    def _receive_damage(self, damage):
        self.statistics.hp -= damage
        
    def get_position(self):
        return self.position

