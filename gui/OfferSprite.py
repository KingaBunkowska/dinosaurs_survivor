import pygame
from utils.ImageLoader import ImageLoader
from game_mechanics.Courences import Courences

class OfferSprite:
    def __init__(self, pos, cost, text, item, type):
        self.price_font = pygame.font.SysFont(None, 30)
        self.info_font = pygame.font.SysFont(None, 18)
        self.item = item
        self.text = self.info_font.render(text, True, (0, 0, 0))
        self.value = [self.price_font.render(str(v), True, (0,0,0)) for v,_ in cost]
        self.value_image = [ImageLoader.get_pickable_sprite(i.value[0]) for _,i in cost]
        self.pos = pos
        self.bg_colors = [(205, 127, 50), (192, 192, 192), (218, 165, 32)]
        self.pick_bg_colors = [(173, 95, 18), (160, 160, 160), (186, 133, 0)]
        self.button_rect = pygame.Rect(pos.x, pos.y, 250, 150)
        self.type = type
    def draw(self, screen):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.pick_bg_colors[self.type],self.button_rect, border_radius=20)
        else:
            pygame.draw.rect(screen, self.bg_colors[self.type], self.button_rect, border_radius=40)

        screen.blit(self.value_image[0], (self.pos.x + 5,self.pos.y + 5))
        screen.blit(self.value[0],(self.pos.x + 35,self.pos.y + 12))
        screen.blit(self.text, (self.pos.x + 5,self.pos.y + 50))
