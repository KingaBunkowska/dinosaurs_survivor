from game_mechanics.Attack import Attack
import pygame

IMAGES = {"whip" : pygame.image.load('resources/whip_attack.png')}

SIZE_OF_IMAGES = {
    "whip": [100, 100]
}

class Attack_preseter:
    """
    Pygame presenter for Attack class
    """
    def __init__(self, attack:Attack, width=50, height=100):
        """

        :param attack: Drawn attack
        :param width: width of sprite
        :param height: height of sprite
        """
        self.attack = attack
        self.width = width
        self.height = height

        img = pygame.transform.scale(IMAGES['whip'], SIZE_OF_IMAGES['whip'])
        img = pygame.transform.scale(img,SIZE_OF_IMAGES["whip"])
        self.image = pygame.transform.rotate(img, attack.angle)
    def draw(self, screen):
        """
        Draw sprite on screen
        :param screen: Object of screen on witch self is drawn
        :type screen: pygame.display
        """
        screen.blit(self.image, self.attack.position.to_coords())