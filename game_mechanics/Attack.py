import random

from game_mechanics.Position import Position
import math

class Attack:
    def __init__(self, target, caster, speed = 8,attack_range = float('inf'), penetrate=True, accuracy = 0):
        self.position = caster.position.copy()
        self.accuracy = accuracy
        self.angle, self.direction = self.calculate_angle(target)

        self.caster = caster
        self.penetrate = penetrate
        self.range = attack_range
        self.speed = speed
        self.attacked = set()
        self.target = target

    def calculate_damage(self, target):
        if target in self.attacked:
            return 0
        self.attacked.add(target)
        return 3.

    def calculate_angle(self,target):
        vector = target - self.position
        vector.normalized()
        vector += Position(random.uniform(-self.accuracy,self.accuracy),random.uniform(-self.accuracy,self.accuracy))
        return math.degrees(math.atan2(-vector.y, vector.x)), vector
    
    def fly(self):
        self.position += (self.direction * self.speed)
        self.range -= self.speed