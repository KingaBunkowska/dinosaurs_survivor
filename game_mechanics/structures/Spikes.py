from game_mechanics.Dinosaur import Dinosaur
from game_mechanics.structures.Structure import Structure

class Spikes(Structure):
    name = "spikes"
    damage = 5
    trigger_distance = 100

    def __init__(self, position):
        super().__init__(position)

    def trigger(self, entity):
        if self.exist and isinstance(entity, Dinosaur) and entity.ally==0 and self.position.distance(entity.position) < self.trigger_distance:
            self.on_trigger(entity)

    def on_trigger(self, trigering_entity):
        trigering_entity._receive_damage(self.damage, None) # Enemies would not be invincible for spikes
        self.exist = 0