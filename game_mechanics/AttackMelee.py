from game_mechanics.Position import Position
from game_mechanics.Attack import Attack
import math

class AttackMelee(Attack):
    def __init__(self,target, caster, range):
        super().__init__(target, caster, speed=1, range = range, penetrate=True)
        self.position += (self.direction * (self.range - 3))
        self.range = 4