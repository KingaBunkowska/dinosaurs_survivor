from game_mechanics.active_abilities.ActiveAbility import ActiveAbility
from game_mechanics.structures.Spikes import Spikes

class PutSpikes(ActiveAbility):
    def __init__(self, target, game):
        self.name = "spikes"
        cooldown = 240
        usage = 5
        self.game = game

        super().__init__(cooldown, usage, target)

    def use(self):
        self.game.add_structure(Spikes(self.target.position))
        self.consume()