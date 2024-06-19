from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Position import Position
from game_mechanics.active_abilities.ActiveAbility import ActiveAbility
import random

class Multiattack(ActiveAbility):
    def __init__(self, target, game):
        self.name = "multiattack"
        self.game = game
        cooldown = 500
        usage = None

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            for i in range(8):
                pass
            self.consume()