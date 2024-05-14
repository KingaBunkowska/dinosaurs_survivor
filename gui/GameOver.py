import pygame

BACKGROUND = (0, 0, 0)
TEXT = (255, 255, 255)

class GameOver:
    def __init__(self):
        font = pygame.font.Font(None, 64)
        self.text_surface = font.render("Game Over!", True, TEXT)

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()
        screen.fill(BACKGROUND)
        text_rect = self.text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(self.text_surface, text_rect)
