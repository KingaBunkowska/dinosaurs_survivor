from game_mechanics.Attack import Attack
from gui.AttackSprite import AttackSprite
import pygame

class LaserAttackSprite(AttackSprite):
    def __init__(self, attack:Attack, attack_type = "laser"):
        self.attack = attack
        self.colision_point = self.attack.position
        self.colision_time = 0

    def draw(self, screen):
        self.colision_time += 1
        if self.colision_time == 2:
            self.colision_point = self.attack.target.position
        pygame.draw.line(screen,(245,0,0),self.attack.caster.position.to_coords(),self.attack.target.position.to_coords(),8)