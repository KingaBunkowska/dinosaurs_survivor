from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Position import Position
import random

from game_mechanics.active_abilities.BulletsCircle import BulletsCircle
from game_mechanics.active_abilities.SpawnDinos import SpawnDinos

class Boss(Dinosaur):
    def __init__(self, game, type=DinosaurType.POLONOSUCHUS):
        initial_position = Position(0, 800)
        statistics = type.value["statistics"].changed_by(hp=200, contact_damage=5)
        super().__init__(type=type, friendly=False ,position=initial_position)
        self.statistics = statistics
        self.abilities = [SpawnDinos(self, game), BulletsCircle(self, game)]
        self.abilities[0].curr_cooldown = 0
        self.using_ability_in = -1
        self.ability_to_use = self.abilities[0]

    def use_abilities(self):
            for ability in self.abilities:
                if ability.can_use() and random.randint(0,4)==0:
                    ability.use()

    def decrease_cooldown(self):
         for ability in self.abilities:
            ability.tick_actions()

    def move(self, player_position: Position, dinosaurs):
        self.use_abilities()
        self.decrease_cooldown()
        # if self.using_ability_in < 0:
        super().move(player_position, dinosaurs)