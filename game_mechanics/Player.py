from game_mechanics.Entity import Entity
from game_mechanics.Statistics import Statistics
from game_mechanics.Inventory import Inventory
from game_mechanics.Coin import Coin

class Player(Entity):
    def __init__(self):
        super().__init__(statistics=Statistics(speed=10, hp = 10., contact_damage=0.))
        self.invincibility = 0
        self.experience = 0
        self.inventory = Inventory()

    def _receive_damage(self, damage, invincibility):
        if self.invincibility == 0:
            self.statistics.hp -= damage
            self.invincibility = invincibility

    def _use_up_invincibility(self):
        if self.invincibility > 0:
            self.invincibility -= 1

    def increase_max_health(self, value):
        percent_of_change = (self.statistics.max_hp + value)/self.statistics.max_hp
        self.statistics.max_hp += value
        self.statistics.hp *= percent_of_change 
        