from game_mechanics.Position import Position
from utils.ImageLoader import ImageLoader
import pygame

BLACK = (0, 0, 0)

class LevelUpMenu:
    def __init__(self, level, choice = True):
        image = None
        self.level = level
        self.choice = choice
        self.font = pygame.font.SysFont(None, 30)
        self.basic = [self.font.render('HP UP (4)', True, BLACK),self.font.render('SPEED UP (5)', True, BLACK),self.font.render('DAMAGE UP (6)', True, BLACK)]
        self.first_class = [self.font.render('Rifle (4)', True, BLACK),self.font.render('Pickaxe (5)', True, BLACK)]
        self.second_class_melee = [self.font.render('Blowtorch (4)', True, BLACK), self.font.render('Chakra (5)', True, BLACK)]
        self.second_class_gun = [self.font.render('Laser (4)', True, BLACK), self.font.render('Shotgun (5)', True, BLACK)]

    def draw(self,screen):
        width, height = screen.get_width(), screen.get_height()
        if self.level == 5:
            screen.blit(self.first_class[0],((width // 2) - 150,height //4))
            screen.blit(self.first_class[1],((width // 2) +  150,height //4))
        elif self.level == 10 and self.choice:
            screen.blit(self.second_class_gun[0], ((width // 2) - 150,height //3))
            screen.blit(self.second_class_gun[1], ((width // 2) +  150,height //3))
        elif self.level == 10 and not self.choice:
            screen.blit(self.second_class_melee[0], ((width // 2) - 150,height //3))
            screen.blit(self.second_class_melee[1], ((width // 2) +  150,height //3))
        else :
            screen.blit(self.basic[0], ((width // 2) - 250,height //4))
            screen.blit(self.basic[1], ((width // 2) - 100,height //4))
            screen.blit(self.basic[2], ((width // 2) + 100,height //4))