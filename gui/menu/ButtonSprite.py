import pygame
from game_mechanics.Position import Position

class ButtonSprite:
    def __init__(self,pos,text,button_width = 370, button_height = 80):
        self.colors = [(139, 69, 19), (205, 133, 63), (255, 215, 0), (169, 169, 169)]
        self.font = pygame.font.Font(None, 64)
        self.text = text

        self.button_rect = pygame.Rect((pos.x + button_width//2) // 2 + 50, (pos.y + button_height//2) // 2 + 50,
                                  button_width, button_height)

    def draw(self,screen):
        pygame.draw.rect(screen, self.colors[3], self.button_rect, border_radius=0)
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.colors[0], self.button_rect, border_radius=20)
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