from game_mechanics.Position import Position
from utils.ImageLoader import ImageLoader
import pygame

BLACK = (0, 0, 0)

class LevelUpMenu:
    def __init__(self, level, choice = True):
        image = None
        self.level = level
        self.choice = choice
        self.font = pygame.font.SysFont(None, 34)
        self.basic = [self.font.render('HP UP (1)', True, BLACK),self.font.render('SPEED UP (2)', True, BLACK),self.font.render('DAMAGE UP (3)', True, BLACK)]
        self.first_class = [self.font.render('Rifle (1)', True, BLACK),self.font.render('Pickaxe (2)', True, BLACK)]
        self.second_class_melee = [self.font.render('Blowtorch (1)', True, BLACK), self.font.render('Chakra (2)', True, BLACK)]
        self.second_class_gun = [self.font.render('Laser (1)', True, BLACK), self.font.render('Shotgun (2)', True, BLACK)]

    def draw(self,screen):
        if self.level == 5:
            screen.blit(self.first_class[0],(40,40))
            screen.blit(self.first_class[1],(240,40))
        elif self.level == 10 and self.choice:
            screen.blit(self.second_class_gun[0], (40, 40))
            screen.blit(self.second_class_gun[1], (240, 40))
        elif self.level == 10 and not self.choice:
            screen.blit(self.second_class_melee[0], (40, 40))
            screen.blit(self.second_class_melee[1], (240, 40))
        else :
            screen.blit(self.basic[0], (40, 40))
            screen.blit(self.basic[1], (240, 40))
            screen.blit(self.basic[2], (440, 40))