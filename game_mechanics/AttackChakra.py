from game_mechanics.Attack import Attack

class AttackChakra(Attack):
    def __init__(self,target, caster, attack_range, speed):
        super().__init__(target, caster, speed=speed, attack_range = attack_range, penetrate=True)
        self.max_range = attack_range//2
        self.reverse = False
    def fly(self):
        super().fly()
        if self.max_range > self.range and not self.reverse:
            self.reverse = True
            self.direction *= -1