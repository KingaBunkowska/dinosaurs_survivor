from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
from utils.ImageLoader import ImageLoader
from gui.AttackSprite import AttackSprite
import pygame

class LaserAttackSprite(AttackSprite):
    """
    Pygame presenter for Attack class
    """
    def __init__(self, attack:Attack, attack_type = "laser"):
        """
        :param attack: Drawn attack
        :param width: width of sprite
        :param height: height of sprite
        """
        self.attack = attack
        self.colision_point = self.attack.position
        self.colision_time = 0


        #self.image = pygame.transform.rotate(self.image, attack.angle)
    def draw(self, screen):
        """
        Draw sprite on screen
        :param screen: Object of screen on witch self is drawn
        :type screen: pygame.display
        """
        self.colision_time += 1
        if self.colision_time == 2:
            self.colision_point = self.attack.target.position
        pygame.draw.line(screen,(245,0,0),self.attack.caster.position.to_coords(),self.attack.target.position.to_coords(),8)