from game_mechanics.Attack import Attack
from game_mechanics.Position import Position
from utils.ImageLoader import ImageLoader
import pygame

class AttackSprite:
    """
    Pygame presenter for Attack class
    """
    def __init__(self, attack:Attack, attack_type = "bullet"):
        """
        :param attack: Drawn attack
        :param width: width of sprite
        :param height: height of sprite
        """
        self.attack = attack
        self.rotate = False
        if attack_type != "laser":
            if attack_type == "blade":
                self.rotate = True
            self.colision_counter = -1
            self.image = ImageLoader.get_projectile_sprite(attack_type)
            self.image = pygame.transform.rotate(self.image, attack.angle)
            self.size, _ = self.image.get_size()

            self.colision_point = Position(self.attack.position.x + self.size / 2,
                                           self.attack.position.y + self.size / 2) + attack.direction * (self.size // 2)
        else:
            self.colision_point = Position(-1000,-1000)
            self.colision_counter = 0
        #self.image = pygame.transform.rotate(self.image, attack.angle)
    def draw(self, screen):
        """
        Draw sprite on screen
        :param screen: Object of screen on witch self is drawn
        :type screen: pygame.display
        """
        if self.colision_counter<0:
            if self.rotate:
                self.image = pygame.transform.rotate(self.image,2)
            self.colision_point = Position(self.attack.position.x + self.size / 2,
                                           self.attack.position.y + self.size / 2) + self.attack.direction * (self.size // 2)
            screen.blit(self.image, (self.attack.position.to_coords()))
        else:
            self.colision_counter += 1
            if self.colision_counter >= 2:
                self.colision_point = self.attack.target
            pygame.draw.line(screen, (245, 0, 0), self.attack.caster.position.to_coords(),
                             self.attack.target.to_coords(), 5)
            pygame.draw.circle(screen,(255,255,0),self.colision_point.to_coords(),5,5)