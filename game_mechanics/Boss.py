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
        # self.abilities = [SpawnDinos(self, game)]
        self.abilities = [Dash(self)]
        self.abilities[0].cooldown = 100
        self.using_ability_in = -1
        self.ablity_to_use = None

    def use_abilities(self):
        # print(self.using_ability_in)
        # if self.using_ability_in >= 0:
        #     self.using_ability_in -= 1
        #     if self.using_ability_in == -1:
        #         self.ability_to_use.use()
        #         print("zrobione")
        # else:
        for ability in self.abilities:
            # if ability.can_use():
                # self.using_ability_in = 30
                # self.ability_to_use = ability
            ability.use()

    def move(self, player_position: Position, dinosaurs):
        self.use_abilities()
        # print(self.using_ability_in)
        # if self.using_ability_in < 0:
        #     print("poruszenie")
        super().move(player_position, dinosaurs)