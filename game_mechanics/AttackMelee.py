from game_mechanics.Attack import Attack

class AttackMelee(Attack):
    def __init__(self,target, caster, attack_range):
        super().__init__(target, caster, speed=1, attack_range = attack_range, penetrate=True)
        self.position += (self.direction * (self.range - 3))
        self.range = 4