from game_mechanics.Entity import Entity
from game_mechanics.Statistics import Statistics
from game_mechanics.Position import Position

class Player(Entity):
    def __init__(self):
        super().__init__(statistics=Statistics(speed=10,hp = 10., contact_damage=0.),position=Position(750,330),facing_right=True)
        self.invincibility = 0
        self.experience = 0
        self.level = 1
        self.last_level_reward = 1
        self.level_function = lambda x: x**(3/2)

    def receive_damage(self, damage, invincibility):
        if self.invincibility == 0:
            self.statistics.hp -= damage
            self.invincibility = invincibility

    def use_up_invincibility(self):
        if self.invincibility > 0:
            self.invincibility -= 1

    def get_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level_function(self.level * 10):
            self.level+=1
            return True
        return False

    def stat_up(self,value,stat):
        if stat == 1:
            self.increase_max_health(value)
        elif stat == 2:
            self.statistics.speed_up(value//2)
        else:
            self.statistics.damage_up(value)

    def increase_max_health(self, value):
        percent_of_change = (self.statistics.max_hp + value)/self.statistics.max_hp
        self.statistics.max_hp += value
        self.statistics.hp *= percent_of_change 
        self.statistics.hp = min(self.statistics.max_hp, self.statistics.hp//1)
       
