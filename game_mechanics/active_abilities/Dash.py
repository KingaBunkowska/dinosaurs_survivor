from game_mechanics.active_abilities.ActiveAbility import ActiveAbility


class Dash(ActiveAbility):
    def __init__(self, target):
        self.name = "dash"
        cooldown = 240
        usage = None

        super().__init__(cooldown, usage, target)

    def use(self):
        if self.can_use():
            self.target.position += self.target.last_move_vector * 300
            self.consume()
