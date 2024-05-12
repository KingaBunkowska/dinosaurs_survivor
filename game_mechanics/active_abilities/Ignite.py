from game_mechanics.active_abilities.ActiveAbility import ActiveAbility

class Ignite(ActiveAbility):
    def __init__(self, player, dinosaurs):
        self.name = "ignite"
        cooldown = 600
        usage = None

        self.player = player
        self.dinosaurs = dinosaurs

        super().__init__(cooldown, usage, None)

    def use(self):
        if self.can_use():
            targets = [dinosaur for dinosaur in self.dinosaurs if dinosaur.position.distance(self.player.position)<200 and not dinosaur.ally]
            self.consume()
