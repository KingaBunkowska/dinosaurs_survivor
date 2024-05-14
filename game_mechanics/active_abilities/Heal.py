from game_mechanics.active_abilities.ActiveAbility import ActiveAbility


class Heal(ActiveAbility):
    def __init__(self, target):
        self.name = "heal"
        cooldown = 600
        usage = 3

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            self.target.statistics.hp = min(self.target.statistics.hp + self.target.statistics.max_hp * 0.5, self.target.statistics.max_hp)
            self.consume()
