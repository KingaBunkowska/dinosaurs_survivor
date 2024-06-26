from game_mechanics.active_abilities.ActiveAbility import ActiveAbility

class Fire(ActiveAbility):
    name = "fire"
    def __init__(self, player, game):
        
        cooldown = 360
        usage = None
        self.player = player

        super().__init__(cooldown, usage, None)

    def use(self, dinosaurs_sprites=[]):
        if self.can_use():
            targets = [dinosaur for dinosaur in [dinosaur_sprite.dinosaur for dinosaur_sprite in dinosaurs_sprites] if dinosaur.position.distance(self.player.position)<100 and not dinosaur.ally]
            for target in targets:
                target.receive_damage(1)
            self.consume()
