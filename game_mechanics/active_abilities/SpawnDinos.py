from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Position import Position
from game_mechanics.active_abilities.ActiveAbility import ActiveAbility
import random

class SpawnDinos(ActiveAbility):
    def __init__(self, target, game):
        self.name = "spawn"
        self.game = game
        cooldown = 1000
        usage = 5

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            for _ in range(random.randint(2,8)):
                self.game._add_dinosaur(Dinosaur(DinosaurType.SILESAURUS, False, position=self.target.position + Position(random.randint(-300, 300), random.randint(-40, 40))))
            self.consume()