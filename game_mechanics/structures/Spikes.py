

from game_mechanics.Dinosaur import Dinosaur


def Spikes(Structure):

    damage = 5
    trigger_distance = 20

    def triger_condition(self, entity):
        return isinstance(entity, Dinosaur) and not entity.ally and self.position.distance(entity.position) < trigger_distance
    
    def on_trigger(self, trigering_entity):
        trigering_entity._receive_damage(damage, self)
        exist = 0