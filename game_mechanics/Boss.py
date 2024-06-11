from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.DinosaurType import DinosaurType
from game_mechanics.Entity import Entity
from game_mechanics.Position import Position
import random

from game_mechanics.active_abilities.Dash import Dash
from game_mechanics.active_abilities.SpawnDinos import SpawnDinos

class Boss(Dinosaur):
    def __init__(self, game, type=DinosaurType.POLONOSUCHUS):
        initial_position = Position(0, 800)
        statistics = type.value["statistics"].changed_by(hp=20, contact_damage=5)
        super().__init__(type=type, friendly=False ,position=initial_position)
        self.statistics = statistics
        self.abilities = [SpawnDinos(self, game)]
        self.abilities[0].curr_cooldown = 0
        self.using_ability_in = -1
        self.ability_to_use = self.abilities[0]

    def use_abilities(self):
        # print(self.using_ability_in)
        if self.using_ability_in >= 0:
            self.using_ability_in -= 1
            if self.using_ability_in == -1:
                self.ability_to_use.use()
                print("JEST")
        else:
            for ability in self.abilities:
                if ability.can_use() and random.randint(0,4)==0:
                    self.using_ability_in = 30
                    self.ability_to_use = ability
                ability.use()

    def move(self, player_position: Position, dinosaurs):
        self.use_abilities()
        if self.using_ability_in < 0:
            super().move(player_position, dinosaurs)