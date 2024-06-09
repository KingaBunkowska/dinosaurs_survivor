import pygame
from utils.ImageLoader import ImageLoader

class OfferSprite:
    def __init__(self, pos, cost, text, item, type):
        self.item = item
        self.value = [v for v,_ in cost]
        self.value_image = [i for _,i in cost]
        self.pos = pos
        self.bg_colors = [(205, 127, 50), (192, 192, 192), (218, 165, 32)]
        self.pick_bg_colors = [(173, 95, 18), (160, 160, 160), (186, 133, 0)]
        self.button_rect = pygame.Rect((pos.x + 300 // 2) // 2, (pos.y + 200 // 2) // 2,
                                       300, 200)
        self.type = type
    def draw(self, screen):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.pick_bg_colors[self.type],self.button_rect, border_radius = 20)
        else:
            pygame.draw.rect(screen, self.bg_colors[self.type], self.button_rect, border_radius=20)
