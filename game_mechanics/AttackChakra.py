from game_mechanics.Position import Position
from game_mechanics.Attack import Attack
import math

class AttackChakra(Attack):
    def __init__(self,target, caster, range, speed):
        super().__init__(target, caster, speed=4, range = range, penetrate=True)
        self.range = range
        self.max_range = range//2
        self.reverse = False
    def fly(self):
        super().fly()
        if self.max_range > self.range and not self.reverse:
            self.reverse = True
            self.direction *= -1