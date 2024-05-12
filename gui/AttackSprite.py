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
        self.image = ImageLoader.get_projectile_sprite(attack_type)
        self.image = pygame.transform.rotate(self.image, attack.angle)
        self.size, _ = self.image.get_size()

        self.colision_point = Position(self.attack.position.x + self.size / 2,
                                       self.attack.position.y + self.size / 2) + attack.direction * (self.size // 2)

        #self.image = pygame.transform.rotate(self.image, attack.angle)
    def draw(self, screen):
        """
        Draw sprite on screen
        :param screen: Object of screen on witch self is drawn
        :type screen: pygame.display
        """
        self.colision_point = Position(self.attack.position.x + self.size / 2,
                                       self.attack.position.y + self.size / 2) + self.attack.direction * (self.size // 2)
        screen.blit(self.image, (self.attack.position.to_coords()))