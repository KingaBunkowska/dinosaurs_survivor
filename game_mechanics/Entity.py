from game_mechanics.Position import Position

class Entity:

    invincibility_base_time = 60

    def __init__(self, statistics = None, position = Position(200, 200), facing_right=False):
        self.statistics = statistics
        self.position = position
        self.original_facing_right = facing_right
        self.facing_right = facing_right

        self.last_move_vector = Position(0, 1)
        self.slowed_down = False
        self.invincibility = {}


    def move(self, move_vector:Position):
        move_vector.normalized()
        self.last_move_vector = move_vector if move_vector.x != 0 or move_vector.y != 0 else self.last_move_vector

        move_vector *= self.statistics.speed
        
        if self.slowed_down:
            move_vector *= 0.5

        self.position += move_vector

        self.position.inside_screen()
        
        if move_vector.to_coords()[0] > 10**-3:
            self.facing_right = not self.original_facing_right
        else:
            self.facing_right = self.original_facing_right

    def _receive_damage(self, damage, dealer=None):
        if ((dealer != None and dealer in self.invincibility.keys() and self.invincibility[dealer] < 1) 
            or dealer == None
            or (dealer != None and dealer not in self.invincibility.keys())):

            self.statistics.hp -= damage
            if dealer != None:
                self.invincibility[dealer] = self.invincibility_base_time

    def get_position(self):
        return self.position
    
    def is_dead(self):
        return self.statistics.hp < 0

    def _use_up_invincibility(self):
        to_delete = []
        for dealer in self.invincibility.keys():
            # cleaning directory if dealer did not deal damage for 60000 ticks (100s for 60FPS)
            if dealer.is_dead() or self.invincibility[dealer] < -60000:
                to_delete.append(dealer)
            else:
                self.invincibility[dealer] -= 1

        [self.invincibility.pop(dealer) for dealer in to_delete]
