import pygame
from gui.Sprite import Sprite

class ButtonSprite(Sprite):
    def __init__(self,pos,off_pos,text,button_width = 200, button_height = 50):
        self.colors = [(139, 69, 19), (205, 133, 63), (255, 215, 0), (169, 169, 169)]
        self.font = pygame.font.Font(None, 64)
        self.text = text

        self.button_rect = pygame.Rect((pos.x + off_pos[0] - button_width // 2),
                                       (pos.y + off_pos[1] - button_height // 2),
                                       button_width, button_height)



    def draw(self,screen):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.colors[0],self.button_rect, border_radius=20)
        else:
            pygame.draw.rect(screen, self.colors[1], self.button_rect, border_radius=20)
        # Draw button


        text_surf = self.font.render(self.text, True, self.colors[2])
        text_rect = text_surf.get_rect(center = self.button_rect.center)
        screen.blit(text_surf, text_rect)

        pygame.draw.circle(screen, self.colors[2], self.button_rect.topleft, 6)
        pygame.draw.circle(screen, self.colors[2], self.button_rect.topright, 6)
        pygame.draw.circle(screen, self.colors[2], self.button_rect.bottomleft, 6)
        pygame.draw.circle(screen, self.colors[2], self.button_rect.bottomright, 6)