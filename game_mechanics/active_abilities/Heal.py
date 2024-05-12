from game_mechanics.active_abilities.ActiveAbility import ActiveAbility


class Dash(ActiveAbility):
    def __init__(self, target):
        self.name = "dash"
        cooldown = 600
        usage = 3

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            self.target.statistics.health += 5
            self.consume()
