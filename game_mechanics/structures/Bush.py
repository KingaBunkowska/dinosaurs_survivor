from game_mechanics.Player import Player
from game_mechanics.structures.Structure import Structure
import random

class Bush(Structure):
    trigger_distance = 100
    healing_power = 5

    def __init__(self, position, game, is_health_bush=True):
        if is_health_bush:
            self.name = "health_bush"
        else:
            self.name = "supply_bush"
        self.is_health_bush = is_health_bush
        self.game = game
        super().__init__(position, game)

    def trigger(self, entity):
        if self.exist and isinstance(entity, Player) and self.position.distance(entity.position) < self.trigger_distance:
            self.on_trigger(entity)

    def on_trigger(self, triggering_entity):
        if self.is_health_bush:
            triggering_entity.statistics.hp = min(triggering_entity.statistics.hp+5, triggering_entity.statistics.max_hp)
        else:
            abilities_with_usage = [ability for ability in self.game.active_abilities if
                                    ability.usages_left is not None]
            if len(abilities_with_usage) != 0:
                ability_to_increase_usage = random.randint(0, len(abilities_with_usage)-1)
                abilities_with_usage[ability_to_increase_usage].usages_left += 1
        self.exist = 0