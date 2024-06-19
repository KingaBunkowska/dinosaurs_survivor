from game_mechanics.PickableItems import PickableItems
from game_mechanics.Weapon import Weapon

class PickableWeapons(PickableItems):
    def __init__(self, position, weapon):
        super().__init__(position)
        self.weapon = weapon

    def on_pick(self, game):
        print("wywolane")
        print(self.weapon, "to jest self.weapon")
        game.weapon = self.weapon
