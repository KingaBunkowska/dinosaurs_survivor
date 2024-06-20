from game_mechanics.active_abilities.ActiveAbility import ActiveAbility


class SlowDownTime(ActiveAbility):
    name = "slow_down_time"
    def __init__(self, player, game):
        cooldown = 1200
        usage = 2
        self.player = player
        self.game = game

        self.percent_of_slow_down = 0.5
        self.duration = 300

        super().__init__(cooldown, usage)

    def use(self):
        if self.can_use():
            self.player.slowed_down = True
            for dino_sprite in self.game.dinosaur_sprites:
                dino_sprite.dinosaur.slowed_down = True
            self.consume()

    def deactivate(self):
        self.player.slowed_down = False
        for dino_sprite in self.game.dinosaur_sprites:
            dino_sprite.dinosaur.slowed_down = False

